from django.contrib import admin

import users.models as users
import products.models as products


class BasketInline(admin.TabularInline):
    model = products.Basket
    extra = 0


@admin.register(users.User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('password', )
    inlines = (BasketInline, )


admin.site.register(users.EmailVerification)
