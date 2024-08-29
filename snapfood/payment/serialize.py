from .models import Copun
from rest_framework.serializers import ModelSerializer

class CopunSerializer(ModelSerializer):
    class Meta:
        model = Copun
        fields = "__all__"