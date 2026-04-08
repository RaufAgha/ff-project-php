from django.core.management.base import BaseCommand
from categories.models import Category


class Command(BaseCommand):
    help = "Seed default categories"

    def handle(self, *args, **kwargs):
        categories = [
            # income
            {"name": "Salary", "type": "income"},
            {"name": "Freelance", "type": "income"},

            # expense
            {"name": "Food", "type": "expense"},
            {"name": "Transport", "type": "expense"},
            {"name": "Utilities", "type": "expense"},
            {"name": "Entertainment", "type": "expense"},
            {"name": "Health", "type": "expense"},
        ]

        for cat in categories:
            obj, created = Category.objects.get_or_create(
                name=cat["name"],
                type=cat["type"]
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {obj.name}"))