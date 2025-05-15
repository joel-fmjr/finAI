from celery import shared_task

from core.models import UploadedFile
from core.services import FileProcessor


@shared_task
def process_file_task(file_id):
    processed_file = UploadedFile.objects.filter(id=file_id).first()
    if not processed_file:
        return {'error': 'File not found'}

    processor = FileProcessor(processed_file)
    processor.run()
    return {'success': True, 'file_id': file_id}
