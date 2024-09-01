from django.views.generic import TemplateView

class CartView(TemplateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    template_name = "ecom/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
