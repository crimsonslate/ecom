from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from ecom.models.product import Product

def get_github_link(request: HttpRequest) -> HttpResponse:
    repo_link = settings.ECOM_USERDATA.LINKS.get("REPOSITORY", "/")
    return redirect(repo_link)


class ShopView(View):
    template_name = "ecom/shop.html"
    partial_template_name = "ecom/partials/shop.html"
    base_context = {
        "title": "Shop",
        "userdata": settings.ECOM_USERDATA,
    }

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, context=self.base_context)

    def post(self, request: HttpRequest) -> HttpResponse:
        if request.htmx:
            return render(
                request, self.partial_template_name, context=self.base_context
            )
        else:
            return render(request, self.template_name, context=self.base_context)
