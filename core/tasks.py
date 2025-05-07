from celery import shared_task

from core.services.process_file import process_file, process_markdown_with_llm


@shared_task
def process_markdown_with_llm_task(markdown_text, file_id):
    return process_markdown_with_llm(markdown_text, file_id)


@shared_task
def process_file_task(file_id):
    result = process_file(file_id)
    process_markdown_with_llm_task.delay(result, file_id)
