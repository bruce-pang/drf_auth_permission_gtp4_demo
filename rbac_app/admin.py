# rbac_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from .models import User, Role, UserRole, RolePermission, TaskExecRecord

class UserAdmin(BaseUserAdmin):
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(RolePermission)
admin.site.register(Permission)

admin.site.register(TaskExecRecord)