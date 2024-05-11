from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AppsViewSet, PublisherViewSet


app_router = DefaultRouter()
app_router.register("apps", AppsViewSet, basename="apps")
app_router.register("publisher", PublisherViewSet, basename="publisher")

urlpatterns = [
    path("", include(app_router.urls)),
]
