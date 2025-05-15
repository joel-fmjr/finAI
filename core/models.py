from django.db import models


class UploadedFile(models.Model):
    class FileType(models.TextChoices):
        FATURA = 'FATURA'
        EXTRATO = 'EXTRATO'

    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=FileType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    markdown_data = models.TextField(null=True, blank=True)
    json_data = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        app_label = 'core'
        verbose_name = 'Uploaded File'
        verbose_name_plural = 'Uploaded Files'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ['-created_at']
        app_label = 'core'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        CREDIT = 'CREDIT'
        DEBIT = 'DEBIT'

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)
    transaction_type = models.CharField(
        max_length=10, choices=TransactionType.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source_file = models.ForeignKey(
        UploadedFile, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ['-date']
        app_label = 'core'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.date} - {self.description} - {self.amount}'
