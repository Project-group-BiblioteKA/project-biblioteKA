from rest_framework import serializers

from users.models import User
from .models import Book
from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "synopse", "author", "amount"]

    def create(self, validated_data):
        num_copies = validated_data["amount"]
        book = Book.objects.create(**validated_data)
        for i in range(num_copies):
            Copy.objects.create(books=book, is_available=True)
        return book

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ["id", "user"]
        read_only_fields = ["id", "user"]


class BookNewSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "synopse",
            "author",
            "amount",
            "book_follow",
        ]
        read_only_fields = [
            "id",
            "title",
            "synopse",
            "author",
            "amount",
            "book_follow",
        ]
        depth = 1
