from decimal import Decimal
from django import forms

from ecom.models import Product

class ProductCreationForm(forms.Form):
    template_name = "ecom/forms/create_product.html"

    name = forms.CharField(label="Product Name", max_length=64)
    desc = forms.CharField(label="Product Description", max_length=2048)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal(0.00), max_value=Decimal(999_999_999.00))
    date_created = forms.DateTimeField()
    date_last_modified = forms.DateTimeField()
    visibility = forms.TypedChoiceField(
        choices=Product.Visibility.choices,
        default=Product.Visibility.UNAVAILABLE,
        coerce=str()
    )
