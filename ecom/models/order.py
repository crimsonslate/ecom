from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from ecom.models.product import Product


class Order(models.Model):
    """A single purchase."""

    class Status(models.TextChoices):
        CREATED = "CRE", _("Order was created.")
        CANCELED = "CAL", _("Order was canceled.")
        FULFILLED = "FUL", _("Products were delivered to customer.")
        SHIPPING = "SHP", _("Order is being shipped.")

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    note = models.TextField(max_length=2048, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=3,
        choices=Status,
        default=Status.CREATED,
    )

    def get_product_by_id(self, product_id: int) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValueError(f"No product with {product_id = } exists.")

    @transaction.atomic
    def update_status(self, new_status: Status) -> None:
        self.update(status=new_status.value)
        self.save()

    @transaction.atomic
    def add_product(self, product_id: int, quantity: int = 1) -> None:
        """Adds any quantity of :model:`ecom.Product`s (by id). Quantity must be a positive integer."""
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        product = self.get_product_by_id(product_id)
        order_item, created = OrderItem.objects.get_or_create(
            order=self, product=product
        )
        if created:
            order_item.quantity = quantity
            order_item.save()
        else:
            order_item.quantity += quantity
            order_item.save()

        return None

    def __str__(self) -> str:
        return f"#{self.id} - {self.date_created:%c} - {self.user.username}"


class OrderItem(models.Model):
    """Represents a :model:`ecom.Product` and its quantity in an :model:`ecom.Order`."""

    order = models.ForeignKey("Order", related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name}"
