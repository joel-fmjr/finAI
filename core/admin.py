from django.contrib import admin

from .models import Category, Transaction, UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'file_type',
        'created_at',
        'is_processed',
        'processed_at',
    )
    list_filter = ('file_type', 'is_processed', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'processed_at')
    date_hierarchy = 'created_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'description',
        'amount',
        'transaction_type',
        'category',
        'source_file',
    )
    list_filter = ('transaction_type', 'category', 'date', 'source_file')
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date'
    list_per_page = 20
