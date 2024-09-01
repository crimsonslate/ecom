from django.views.generic import CreateView

from ecom.models import Product

class ProductCreateView(CreateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    fields = ["name", "desc", "visibility", "price", "category"]
    model = Product
    queryset = Product.objects.filter(visibility__exact="VIS").all()
