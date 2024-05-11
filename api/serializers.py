from rest_framework.serializers import ModelSerializer
from api.models import Apps, Publisher

class AppSerializer(ModelSerializer):
    class Meta:
        model = Apps
        fields = "__all__"


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
