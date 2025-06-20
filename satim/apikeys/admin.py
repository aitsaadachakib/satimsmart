from django.contrib import admin
from .models import APIKey

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'is_active', 'created_at')
    list_filter = ('is_active', 'user')
    search_fields = ('user__username', 'key')
    readonly_fields = ('key', 'created_at')

    def has_add_permission(self, request):
        return request.user.is_superuser
