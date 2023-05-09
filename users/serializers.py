from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from books.serializers import BookSerializer
from .models import *
from django.core.mail import send_mail
from django.conf import settings


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
        if (
            validated_data.get("is_staff") == True
            and not self.context["request"].user.is_superuser
        ):
            raise serializers.ValidationError(
                {"error": "You have no permission to create a collaborator"}
            )
        else:
            user = User.objects.create_user(**validated_data)
            # self.send_confirmation_email(user)
            return user

    # def send_confirmation_email(self, user: User):
    #     subject = "Confirmação de conta"
    #     message = "Olá {0},\n\nSua conta foi criada com sucesso.".format(user.username)
    #     from_email = settings.DEFAULT_FROM_EMAIL
    #     recipient_list = [user.email]
    #     send_mail(subject, message, from_email, recipient_list)

    def create_superuser(self, validated_data: dict) -> User:
        if (
            self.context["request"].user.is_staff
            and self.context["request"].user.is_superuser
        ):
            return User.objects.create_superuser(**validated_data)
        else:
            raise serializers.ValidationError(
                {"error": "You have no permission to create a admin"}
            )

    def update(self, instance: User, validated_data: dict) -> User:
        if (
            self.context["request"].user.is_staff
            and self.context["request"].user.is_superuser
        ) or validated_data.get("is_staff") == None:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.set_password(validated_data.get("password", instance.password))
            instance.save()
            return instance

        else:
            raise serializers.ValidationError(
                "you has not permission to modificated the field 'is_staff'"
            )

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
        read_only_fields = ["uuid"]


class FollowerBookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    books = BookSerializer(read_only=True)
    users = UserSerializer(read_only=True)

    class Meta:
        model = BookFollower
        fields = ["id", "books", "users"]
