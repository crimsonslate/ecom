from django.views.generic import DetailView, ListView

from ecom.models import Order

class OrderDetailView(DetailView):
    model = Order

    content_type = "text/html"
    context_object_name = "order"
    extra_context = None
    http_method_names = ["get", "post"]

class OrderListView(ListView):
    model = Order

    content_type = "text/html"
    context_object_name = "orders_list"
    extra_context = None
    http_method_names = ["get", "post"]
