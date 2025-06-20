from django.contrib import admin

# Register your models here.
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transactionid', 'user', 'status', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('transactionid', 'user__username')
    readonly_fields = ('transactionid', 'created_at')
