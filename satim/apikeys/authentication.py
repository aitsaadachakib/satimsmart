from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return None
        try:
            key_obj = APIKey.objects.select_related('user').get(key=api_key, is_active=True)  # type: ignore[attr-defined]
        except APIKey.DoesNotExist:  # type: ignore[attr-defined]
            raise AuthenticationFailed('Invalid or inactive API key')
        return (key_obj.user, None) 