from django.db import models, transaction
from django.contrib.auth.models import User

from ecom.models.product import Product

class CartItem(models.Model):
    """Represents a product in a :model:`ecom.Cart`."""

    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of '{self.product.name}'"

class Cart(models.Model):
    """Holds :model:`ecom.CartItem`s. User is optional."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s cart"

    def get_product_by_id(self, product_id: int) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValueError(f"No product with {product_id = } exists.")

    @transaction.atomic
    def create_order(self) -> None:
        """Creates an :model:`ecom.Order` based on this cart's :model:`ecom.CartItem`s."""
        raise NotImplementedError
        return None

    @transaction.atomic
    def clear_items(self) -> None:
        """Clears the cart of :model:`ecom.CartItem`s."""
        raise NotImplementedError
        self.items.delete()
        self.save()
        return None

    @transaction.atomic
    def add_product(self, product_id: int, quantity: int = 1) -> None:
        """Adds any quantity of :model:`ecom.Product`s by id. Quantity must be a positive integer."""
        if quantity <= 0:
            raise ValueError(f"Invalid quantity '{quantity}'. Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()
        return None

    @transaction.atomic
    def rm_product(self, product_id: int, quantity: int = 1) -> None:
        """Removes any quantity of :model:`ecom.Product`s by id. Quantity must be a positive integer."""
        if quantity <= 0:
            raise ValueError(f"Invalid quantity '{quantity}'. Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        try:
            cart_item = self.items.get(product=product)
        except CartItem.DoesNotExist:
            raise ValueError(f"Product <{product.id}:'{product.name}'> not found in this cart.")

        if quantity > cart_item.quantity:
            raise ValueError(
                f"Invalid quantity '{quantity}'. Quantity cannot be greater than {cart_item.quantity}."
            )
        elif quantity == cart_item.quantity:
            cart_item.delete()
        else:
            cart_item.quantity -= quantity
            cart_item.save()

        return None