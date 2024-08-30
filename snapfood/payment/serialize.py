from .models import Copun ,Transaction , Factor
from rest_framework.serializers import ModelSerializer

class CopunSerializer(ModelSerializer):
    class Meta:
        model = Copun
        fields = "__all__"
        
        
class Transcreate(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class Factorserialize(ModelSerializer):
    class Meta:
        model = Factor
        fields = "__all__"