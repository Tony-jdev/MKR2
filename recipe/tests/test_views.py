from django.test import TestCase, Client
from django.urls import reverse
from recipe.models import Category, Recipe
from django.utils import timezone

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(name="Dessert")
        self.category2 = Category.objects.create(name="Main Course")

        for i in range(15):
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Test description",
                instructions="Test instructions",
                ingredients="Test ingredients",
                created_at=timezone.now(),
                updated_at=timezone.now(),
                category=self.category1 if i % 2 == 0 else self.category2
            )

    def test_main_view(self):
        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['recipes']), 10)

        self.assertTemplateUsed(response, 'main.html')

        self.assertContains(response, '<h1>Recipes</h1>')

    def test_category_detail_view(self):
        category_id = self.category1.id
        response = self.client.get(reverse('category_detail', args=[category_id]))

        self.assertEqual(response.status_code, 200)

        recipes = response.context['category']
        for recipe in recipes:
            self.assertEqual(recipe.category, self.category1)

        self.assertEqual(len(recipes), 8)

        self.assertTemplateUsed(response, 'category_detail.html')

        self.assertContains(response, '<h1>Category List</h1>')

    def test_category_detail_view_not_found(self):
        response = self.client.get(reverse('category_detail', args=[999]))
        self.assertEqual(response.status_code, 404)