import json

from django.contrib import admin

from .models import Category, Transaction, UploadedFile
from .services import FileProcessor


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

    actions = ['persist_transactions', 'process_file']

    def persist_transactions(self, request, queryset):
        for file in queryset:
            processor = FileProcessor(file)
            json_data = json.loads(file.processed_data_json)
            processor.persist_transactions(json_data['context'])

    def process_file(self, request, queryset):
        for file in queryset:
            processor = FileProcessor(file)
            processor.run()


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
