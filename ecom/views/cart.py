from typing import Any

from django.db.models import QuerySet
from django.views.generic import TemplateView
from django.http import HttpResponse

from ecom.models import Cart, CartItem


class CartView(TemplateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    template_name = "ecom/cart.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["items"] = self.get_items()
        return context

    def get_cart(self) -> Cart:
        """Gets, or creates, a :model:`ecom.Cart` depending on user authentication status."""
        if self.request.user is None:
            raise NotImplementedError

        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def get_items(self) -> QuerySet:
        """Returns a queryset of :model:`ecom.CartItem` instances associated with the cart."""
        return CartItem.objects.filter(cart=self.get_cart())

    def get_item(self, product_id: int) -> CartItem:
        """Returns a :model:`ecom.CartItem` instance associated with the cart."""
        items = self.get_items()
        return items.get(product__id=product_id)

    def incr_quantity(self, product_id: int) -> HttpResponse:
        item = self.get_item(product_id)
        item.quantity += 1
        item.save()
        return HttpResponse(status=404)

    def decr_quantity(self, product_id: int) -> HttpResponse:
        item = self.get_item(product_id)
        if item.quantity == 1:
            pass
        else:
            item.quantity -= 1
            item.save()
        return HttpResponse(status=404)

    def set_quantity(self, product_id: int, quantity: int = 1) -> HttpResponse:
        item = self.get_item(product_id)
        if quantity < 0:
            raise ValueError(f"Cannot set '{item.product.name}' to negative quantity.")
        elif quantity == 0:
            item.delete()
        else:
            item.quantity = quantity
        return HttpResponse(status=404)

    def clear_item(self, product_id: int) -> HttpResponse:
        item = self.get_item(product_id)
        item.delete()
        return HttpResponse(status=404)

    def clear_all(self) -> HttpResponse:
        cart = self.get_cart()
        cart.clear_items()
        cart.save()
        return HttpResponse(status=404)

    def checkout(self) -> HttpResponse:
        return HttpResponse(status=404)
