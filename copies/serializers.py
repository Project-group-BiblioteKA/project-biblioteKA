from rest_framework import serializers

from copies.models import LoandBook


class LoandSerializer(serializers.ModelSerializer):
    borrowed_date = serializers.DateField(read_only=True)

    class Meta:
        model = LoandBook
        fields = [
            "id",
            "devolution_date",
            "borrowed_date",
            "copy_id",
            "users_id",
        ]
