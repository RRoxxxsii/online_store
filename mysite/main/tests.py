from django.test import TestCase
from .models import *


class TestDataBase(TestCase):
    fixtures = [
        'main/fixtures/data.json'
    ]

    def setUp(self) -> None:
        self.user = User.objects.get(username='root')

    def test_all_data(self):
        self.assertGreater(Product.objects.all().count(), 0)
        self.assertGreater(Order.objects.all().count(), 0)
        self.assertGreater(ProductCategory.objects.all().count(), 0)
        self.assertGreater(User.objects.all().count(), 0)
        self.assertGreater(OrderItem.objects.all().count(), 0)