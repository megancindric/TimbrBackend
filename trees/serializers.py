from rest_framework import serializers
from .models import Tree

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'common_name', 'scientific_name', 'fact1', 'pickup_line']
        depth = 1
