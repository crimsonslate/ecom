from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>/", views.ProductDetailView.as_view(), name="product detail"),
    path("all/", views.ProductListView.as_view(), name="product list"),
    path("cart/", views.CartView.as_view(), name="cart"),
]
