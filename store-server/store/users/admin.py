from django.contrib import admin

import users.models as users


admin.site.register(users.User)
