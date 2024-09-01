from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic.detail import DetailView

from ecom.models import Product
from ecom.models.forms.product import ProductCreationForm, ProductDeletionForm, ProductUpdateForm

class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    fields = ["name", "desc", "visibility", "price", "category"]
    model = Product
    queryset = Product.objects.all()
    form_class = ProductCreationForm

class ProductDeletionView(DeleteView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Product
    queryset = Product.objects.all()
    form_class = ProductDeletionForm

class ProductUpdateView(UpdateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Product
    queryset = Product.objects.all()
    form_class = ProductUpdateForm
