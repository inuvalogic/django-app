import datetime

from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Category, Blog

# class BlogModelTests(TestCase):
#     def test_was_published_recently_with_future_date(self):
#         """
#         was_published_recently() returns False for blogs
#         whose pub_date is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_blog = Blog(pub_date=time)
#         self.assertIs(future_blog.was_published_recently(), False)

class CategoryTests(TestCase):
    def setUp(self):
        Category.objects.create(name="artikel", enable=True)
        Category.objects.create(name="berita", enable=True)

    def test_category_all_enable(self):
        """all category enable are correctly identified"""
        artikel = Category.objects.get(name="artikel")
        berita = Category.objects.get(name="berita")
        self.assertEqual(artikel.is_enabled(), True)
        self.assertEqual(berita.is_enabled(), True)