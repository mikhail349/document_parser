from rest_framework import serializers


class ReceiptCreateSerializer(serializers.Serializer):
    """Сериализатор парсера файла."""

    document = serializers.FileField()
