from rest_framework.routers import DefaultRouter

from core.api.viewsets import (
    CategoryViewSet,
    TransactionViewSet,
    UploadedFileViewSet,
)

router = DefaultRouter()
router.register(r'file-upload', UploadedFileViewSet, basename='file-upload')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
