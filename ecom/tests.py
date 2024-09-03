from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from ecom.models import Cart, Product

# How many lines can we get this file to?

class CartModelTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test_user",
            email="test_user@domain.com",
            password="test_password",
        )
        self.test_cart = Cart.objects.create(user=self.test_user)

    def test_cannot_add_negative_quantity_to_cart(self):
        """Succeeds if `ValueError` is raised when attempting to add a negative quantity of a product to the test cart."""
        test_product = Product.objects.create(name="test_product_1", price=Decimal(1.00))
        self.assertRaisesMessage(
            ValueError,
            "Invalid quantity '-1'. Quantity must be a positive integer.",
            self.test_cart.add_product,
            product_id=test_product.id,
            quantity=-1
        )

    def test_cannot_rm_negative_quantity_from_cart(self):
        """Succeeds if `ValueError` is raised when attempting to remove a negative quantity of a product from the test cart."""
        test_product = Product.objects.create(name="test_product_1", price=Decimal(1.00))
        self.test_cart.add_product(product_id=test_product.id, quantity=1)
        self.test_cart.save()

        self.assertRaisesMessage(
            ValueError,
            "Invalid quantity '-1'. Quantity must be a positive integer.",
            self.test_cart.rm_product,
            product_id=test_product.id,
            quantity=-1
        )
