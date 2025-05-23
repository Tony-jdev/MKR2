from django.core.management.base import BaseCommand
from recipe.models import Recipe, Category
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generates random recipes for the recipe app'

    def handle(self, *args, **options):
        titles = ['Pasta Primavera', 'Chicken Soup', 'Chocolate Cake', 'Caesar Salad', 'Beef Stir-Fry',
                  'Fruit Smoothie', 'Vegetable Curry', 'Apple Pie', 'Tomato Soup', 'Grilled Salmon']
        descriptions = [
            'A delicious and healthy meal.',
            'Warm and comforting dish.',
            'Perfect for any celebration.',
            'Fresh and crunchy salad.',
            'Quick and tasty stir-fry.'
        ]
        instructions = [
            'Cook ingredients and serve hot.',
            'Simmer for 30 minutes and enjoy.',
            'Bake at 180C for 40 minutes.',
            'Mix and chill for 1 hour.',
            'Grill for 10 minutes per side.'
        ]
        ingredients = [
            'Pasta, vegetables, olive oil',
            'Chicken, broth, carrots',
            'Flour, sugar, cocoa, eggs',
            'Lettuce, croutons, dressing',
            'Beef, soy sauce, bell peppers'
        ]

        categories = list(Category.objects.all())

        for _ in range(20):
            title = random.choice(titles)
            description = random.choice(descriptions)
            instruction = random.choice(instructions)
            ingredient = random.choice(ingredients)
            category = random.choice(categories)

            Recipe.objects.get_or_create(
                title=title,
                description=description,
                instructions=instruction,
                ingredients=ingredient,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                category=category
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created recipe: {title}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated all recipes'))