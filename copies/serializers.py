from rest_framework import serializers
from datetime import datetime, timedelta
from copies.models import LoandBook
from users.serializers import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    borrowed_date = serializers.DateField(read_only=True)
    devolution_date = serializers.DateField(read_only=True)

    def create(self, validated_data):
        borrowed_date = datetime.today().date()
        devolution_date = borrowed_date + timedelta(days=7)
        if devolution_date.weekday() == 5:
            devolution_date = devolution_date + timedelta(days=2)
        if devolution_date.weekday() == 6:
            devolution_date = devolution_date + timedelta(days=1)

        loand_book = LoandBook.objects.create(
            copy=validated_data["copy"],
            users=validated_data["users"],
            borrowed_date=borrowed_date,
            devolution_date=devolution_date,
        )

        return loand_book

    class Meta:
        model = LoandBook
        fields = [
            "id",
            "devolution_date",
            "borrowed_date",
            "copy_id",
            "users_id",
            "is_return",
        ]
