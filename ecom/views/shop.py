from django.views.generic import TemplateView



class ShopTemplateView(TemplateView):
    content_type = "html"
    http_method_names = ["get", "post"]

    