from django.core.exceptions import ValidationError
from django.core.files.storage import storages
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField


def validate_slug_is_unique(value: str) -> None:
    """Raises ValidationError if the value would create a non-unique slug."""
    if not Product.objects.get(name=value).exists():
        if Product.objects.get(slug=slugify(value)).exists():
            raise ValidationError(
                _("'%(value)s' would generate a non-unique slug."),
                params={"value": value},
            )

class Product(models.Model):
    """A purchasable item in the store."""

    class Meta:
        ordering = ["-name", "-date_last_modified"]

    class Visibility(models.TextChoices):
        """Visibility states of a product."""

        VISIBLE = "VIS", _("Visible")
        HIDDEN = "HID", _("Hidden")
        UNAVAILABLE = "UNA", _("Unavailable")

    name = models.CharField(max_length=64)
    slug = models.CharField(
        max_length=64, unique=True, validators=[validate_slug_is_unique]
    )
    desc = models.TextField(
        verbose_name="description", max_length=2048, blank=True, default=""
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    visibility = models.CharField(
        max_length=3,
        choices=Visibility,
        default=Visibility.UNAVAILABLE,
    )
    price = MoneyField(max_digits=19, decimal_places=4, default_currency="USD")
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    """Image for a :model:`ecom.Product`."""

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product",
        related_name="images",
        on_delete=models.CASCADE,
    )
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Image #{self.id} for {self.product.name}"


class ProductVideo(models.Model):
    """Video for a :model:`ecom.Product`."""

    class Meta:
        verbose_name = "Product Video"
        verbose_name_plural = "Product Videos"

    name = models.CharField(max_length=64)
    caption = models.CharField(max_length=256)
    product = models.ForeignKey(
        "Product",
        related_name="videos",
        on_delete=models.CASCADE,
    )
    source = models.FileField(storage=storages["bucket"])

    @property
    def url(self) -> str:
        return self.source.url

    def __str__(self) -> str:
        return f"Video #{self.id} for {self.product.name}"


class ProductCategory(models.Model):
    """Categorizes :model:`ecom.Product`s."""

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    name = models.CharField(max_length=64)
    cover_image = models.FileField(storage=storages["bucket"], null=True, default=None)
    logo_image = models.FileField(storage=storages["bucket"], null=True, default=None)
    products = models.ManyToManyField("Product")

    def __str__(self) -> str:
        return self.name
