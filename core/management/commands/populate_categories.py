from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Category


class Command(BaseCommand):
    help = 'Populate Category model with categories from FileProcessor prompt'

    def handle(self, *args, **options):
        categories = [
            'Alimentação',
            'Receitas',
            'Mercado',
            'Saúde',
            'Educação',
            'Compras',
            'Transporte',
            'Investimento',
            'Transferências para terceiros',
            'Telefone',
            'Moradia',
        ]

        self.stdout.write(
            f"Found {len(categories)} categories: {', '.join(categories)}"
        )

        with transaction.atomic():
            created_count = 0
            for category_name in categories:
                category, created = Category.objects.get_or_create(
                    name=category_name
                )
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Created category: {category_name}'
                        )
                    )
                else:
                    self.stdout.write(
                        f'Category already exists: {category_name}'
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created {created_count} new categories'
                )
            )
