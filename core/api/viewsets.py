from rest_framework import status, viewsets
from rest_framework.response import Response

from core.api.serializers import (
    CategorySerializer,
    TransactionSerializer,
    UploadedFileSerializer,
)
from core.models import Category, Transaction, UploadedFile
from core.tasks import process_file_task


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        process_file_task.delay(serializer.instance.pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
