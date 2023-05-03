from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'amount']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance:Book, validated_data:dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        return instance
    

