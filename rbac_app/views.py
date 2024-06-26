from rest_framework import viewsets
from .models import User, Role, Permission, TaskExecRecord
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, TaskExecRecordSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import HasPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # 仅超级管理员可以访问

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]  # 仅超级管理员可以访问

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUser]  # 仅超级管理员可以访问

class TaskExecRecordViewSet(viewsets.ModelViewSet):
    queryset = TaskExecRecord.objects.all()
    serializer_class = TaskExecRecordSerializer
    permission_classes = [IsAuthenticated, HasPermission]