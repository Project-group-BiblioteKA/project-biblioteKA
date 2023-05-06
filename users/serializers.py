from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from books.serializers import BookSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="Username already taken."
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="There is already an account registered to this email.",
            )
        ]
    )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def create_superuser(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data.get("password", instance.password))
        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "is_blocked",
            "books",
        ]
        read_only_fields = ["uuid", "is_superuser"]


class FollowerBookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    books = BookSerializer(read_only=True)
    users = UserSerializer(read_only=True)

    class Meta:
        model = BookFollower
        fields = ["id", "books", "users"]
