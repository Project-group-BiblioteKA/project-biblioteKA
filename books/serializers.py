from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'amount', 'available' ]


    def update(self, instance:Book, validated_data:dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        return instance
    # id=serializers.IntegerField(read_only=True)
    # title=serializers.CharField(max_length=50)
    # description=serializers.CharField()
    # author = serializers.CharField(max_length=50)
    # amount=serializers.IntegerField()
    # available=serializers.IntegerField()


