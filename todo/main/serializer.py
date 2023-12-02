from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        new = Todo.objects.create(**validated_data)
        return new
