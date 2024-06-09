from django.db.models import fields
from rest_framework import serializers
from .models import Elements

class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = ('section', 'category', 'code', 'name', 'price')