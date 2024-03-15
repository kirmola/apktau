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


class AppsDetailView(DetailView):
    model = Apps
    template_name = ".html"
    template_name_suffix = "_detail"