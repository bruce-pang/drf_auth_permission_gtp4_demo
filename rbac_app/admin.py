# rbac_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from .models import User, Role, UserRole, RolePermission, TaskExecRecord

class UserAdmin(BaseUserAdmin):
    """
    在我使用python manage.py createsuperuser创建了admin用户后，通过http://localhost:8000/admin/ 使用admin账号登录报错,是因为在定义自定义用户模型时没有正确地配置 Django 内置的 User 模型相关的部分,这部分需要手动注册接管
    """
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(RolePermission)
admin.site.register(Permission)

admin.site.register(TaskExecRecord)