from rest_framework import serializers
from .models import User, Role, Permission, TaskExecRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class TaskExecRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExecRecord
        fields = '__all__'
