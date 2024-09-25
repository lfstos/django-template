from django.contrib import admin
from core.django_min_custom_user.admin import MinUserAdmin
from core.base.models import User


@admin.register(User)
class UserAdmin(MinUserAdmin):
    pass
