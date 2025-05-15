from rest_framework import status, viewsets
from rest_framework.response import Response

from core.api.serializers import UploadedFileSerializer
from core.models import UploadedFile
from core.tasks import process_file_task


class UploadedFileViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            uploaded_file = UploadedFile.objects.get(pk=pk)
            serializer = UploadedFileSerializer(uploaded_file)
            return Response(serializer.data)
        except UploadedFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            process_file_task.delay(serializer.instance.pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            uploaded_file = UploadedFile.objects.get(pk=pk)
            serializer = UploadedFileSerializer(
                uploaded_file, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except UploadedFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            uploaded_file = UploadedFile.objects.get(pk=pk)
            uploaded_file.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UploadedFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
