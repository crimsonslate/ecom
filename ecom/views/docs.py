from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def get_documentation_page(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    context = {}
    return render(request, "ecom/documentation.html", context=context)

def get_documentation_index(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    context = {}
    return render(request, "ecom/documentation_index.html", context=context)
