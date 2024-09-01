from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic.detail import DetailView

from ecom.models import Product
from ecom.models.forms.product import ProductCreationForm, ProductDeletionForm, ProductUpdateForm

class ProductDetailView(DetailView):
    model = Product

    content_type = "text/html"
    context_object_name = "product"
    extra_context = None
    http_method_names = ["get", "post"]
    queryset = Product.objects.filter(visibility__exact="VIS")

class ProductListView(ListView):
    model = Product

    content_type = "text/html"
    context_object_name = "products_list"
    extra_context = None
    http_method_names = ["get", "post"]
    queryset = Product.objects.filter(visibility__exact="VIS")

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    model = Product

    content_type = "text/html"
    http_method_names = ["get", "post"]
    fields = ["name", "desc", "visibility", "price", "category"]
    queryset = Product.objects.all()

class ProductDeleteView(DeleteView):
    form_class = ProductDeletionForm
    model = Product

    content_type = "text/html"
    http_method_names = ["get", "post"]
    queryset = Product.objects.all()

class ProductUpdateView(UpdateView):
    form_class = ProductUpdateForm
    model = Product

    content_type = "text/html"
    http_method_names = ["get", "post"]
    queryset = Product.objects.all()
