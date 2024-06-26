import redis
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from .models import UserRole, RolePermission

class CacheUserPermissionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            redis_client = redis.StrictRedis.from_url(settings.CACHES['default']['LOCATION'])
            user_key = f"user_permissions_{request.user.id}"
            if not redis_client.exists(user_key):
                roles = UserRole.objects.filter(user=request.user).values_list('role', flat=True)
                permissions = RolePermission.objects.filter(role__in=roles).values_list('permission__codename', flat=True)
                permissions_list = list(permissions)
                redis_client.set(user_key, permissions_list, ex=36000)  # 设置1小时的过期时间
                request.user.permissions = permissions_list
            else:
                request.user.permissions = redis_client.get(user_key)

        return None
