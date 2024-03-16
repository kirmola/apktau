from .urls import *
from django.urls import include

urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),

   
]

