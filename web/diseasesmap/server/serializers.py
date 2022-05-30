from rest_framework import serializers
from server.models import Doencas

class DoencasSerializers(serializers.ModelSerializer):
    class Meta:
        model=Doencas
        fields=('id','nome','descricao','vacinadisp','link')