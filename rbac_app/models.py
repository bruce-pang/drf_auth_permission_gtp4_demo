from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    """
    如果不配置如下的部分，迁移数据库时会报错：
    > python manage.py makemigrations
    SystemCheckError: System check identified some issues:
    ERRORS:
    auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'rbac_app.User.groups'.
            HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'rbac_app.User.groups'.
    auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'rbac_app.User.user_permissions'.
            HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'rbac_app.User.user_permissions'.
    rbac_app.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'rbac_app.User.groups' clashes with reverse accessor for 'auth.User.groups'.
            HINT: Add or change a related_name argument to the definition for 'rbac_app.User.groups' or 'auth.User.groups'.
    rbac_app.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'rbac_app.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
            HINT: Add or change a related_name argument to the definition for 'rbac_app.User.user_permissions' or 'auth.User.user_permissions'.
    """
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='rbac_app_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='rbac_app_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    codename = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} - {self.role.name}'

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.role.name} - {self.permission.name}'

class TaskExecRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField(choices=[(0, '未完成'), (1, '已完成')], default=0)
    result = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'task_exec_record'
        ordering = ['-create_time']
        verbose_name = '任务执行记录'
        verbose_name_plural = '任务执行记录'
    def __str__(self):
        return f'{self.user.username} - {self.task_name}'