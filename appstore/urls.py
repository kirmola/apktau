from django.urls import path
from .views import (
    AppsListView,
    AppsDetailView,
)


urlpatterns = [
    path("apps/", AppsListView.as_view(), name="apps"),
    path("games/", AppsListView.as_view(), name="games"),
    path("apps/<slug:package_id>/", AppsDetailView.as_view(), name="App_detail"),
]
