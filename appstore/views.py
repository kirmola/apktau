from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView
)
from .models import (
    Apps, 
    Publisher
)


class AppsListView(ListView):
    model = Apps
    template_name = ".html"
    template_name_suffix = "_list"


class AppsDetailView(DetailView):
    model = Apps
    template_name_suffix = "_detail"
    slug_field = "app_package_name"     # This refer to database slug field which would be displayed in urls
    slug_url_kwarg = "package_id"       # This is defined in url dispatcher in urls.py

    # def get_queryset(self):
    #     current_app_id = self.kwargs.get("package_id")
    #     return super().get_queryset().filter(app_package_name=current_app_id)
    
    # def get_context_data(self, **kwargs) -> dict[str]:
    #     context = super().get_context_data(**kwargs)
    #     context["app_detail"] = self.get_queryset()
    #     return context
    