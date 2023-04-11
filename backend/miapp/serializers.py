from django.db.models import fields
from rest_framework import serializers
from .models import TestUserModel

class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUserModel
        fields = '__all__'