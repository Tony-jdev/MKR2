from django.core.management.base import BaseCommand
from recipe.models import Category

class Command(BaseCommand):
    help = 'Generates random categories for the recipe app'

    def handle(self, *args, **options):
        category_names = [
            'Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Appetizer',
            'Soup', 'Salad', 'Main Course', 'Snack', 'Beverage'
        ]

        for name in category_names:
            Category.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created category: {name}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated all categories'))