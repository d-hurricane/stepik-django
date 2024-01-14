from datetime import timedelta
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils import timezone

import uuid


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    verified_email_at = models.DateTimeField(null=True)

    def is_verified_email(self):
        return bool(self.verified_email_at)


class EmailVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    code = models.UUIDField()
    register_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Email verification code for {self.user.email}'

    @classmethod
    def create(cls, user):
        record = cls.objects.create(
            user=user,
            code=uuid.uuid4(),
            expiration=timezone.now() + timedelta(days=2),
        )
        record.send_email()

    @classmethod
    def update(cls, user, code):
        record = cls.objects.get(user=user, code=code)
        if not record.is_expiration():
            raise Exception('Код верификации просрочен')
        user.verified_email_at = timezone.now()
        user.save()
        record.delete()

    def send_email(self):
        links_arg = {
            'user': self.user.id,
            'code': self.code,
        }
        link = settings.DOMAIN_URL + reverse('users:verify', kwargs=links_arg)
        subject = f'Подтверждение регистрации'
        message = f'Для подтверждения адреса электронной почты перейдите по ссылке {link}.'
        send_mail(
            from_email='from@example.com',
            subject=subject,
            message=message,
            recipient_list=[self.user.email],
        )

    def is_expiration(self):
        return timezone.now() <= self.expiration
