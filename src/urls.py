from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/docs/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", include("ecom.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
    urlpatterns += staticfiles_urlpatterns()
