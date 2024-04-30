from rest_framework import serializers
from .models import Student, ProductList


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductList
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
