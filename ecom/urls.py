from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductCreateView.as_view(), name="home"),
    path("cart/", views.CartItemListView.as_view(), name="cart"),
    path("<int:product_id>/", views.ProductCreateView.as_view(), name="product"),
    path("all/", views.ProductCreateView.as_view(), name="product list"),
    path("orders/", views.OrderListView.as_view(), name="order list"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order detail"),
]
