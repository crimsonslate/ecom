from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/checkout/", views.CartView.checkout, name="checkout"),
    path("cart/qty/<int:product_id>/<int:quantity>/", views.CartView.set_quantity, name="add to cart"),
    path("cart/qty/<int:product_id>/<int:quantity>/", views.CartView.incr_quantity, name="add to cart"),
    path("cart/qty/<int:product_id>/<int:quantity>/", views.CartView.decr_quantity, name="add to cart"),
    path("cart/clear/<int:product_id>/", views.CartView.clear_item, name="clear item"),
    path("cart/clear/all/", views.CartView.clear_all, name="clear all"),

    path("products/create/", views.ProductCreateView.as_view(), name="product create"),
    path("products/<str:slug>/", views.ProductDetailView.as_view(), name="product detail"),
    path("products/<str:slug>/edit/", views.ProductUpdateView.as_view(), name="product edit"),
    path("products/<str:slug>/rm/", views.ProductDeleteView.as_view(), name="product rm"),

    path("orders/", views.OrderListView.as_view(), name="product list"),
    path("orders/inspect/<int:pk>/", views.OrderDetailView.as_view(), name="order detail"),
    #path("orders/<int:year>/", ...),
    #path("orders/<int:year>/<int:month>/", ...),
    #path("orders/<int:year>/<int:month>/<str:weekday>/", ...),
]
