from rest_framework.routers import DefaultRouter

from core.api.viewsets import (
    CategoryViewSet,
    TransactionViewSet,
    UploadedFileViewSet,
)

router = DefaultRouter()
router.register(r'file-upload', UploadedFileViewSet)
# router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)
