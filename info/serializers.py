from rest_framework import serializers
from info.models import Graph

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['x','y']
        model = Graph
