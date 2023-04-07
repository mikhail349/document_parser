import logging

from rest_framework import generics, status
from rest_framework.response import Response

from receipts.serializers import ReceiptCreateSerializer
from services.parser import get_parser


class ReceiptAPIView(generics.GenericAPIView):
    """API парсера файла."""

    serializer_class = ReceiptCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)

        parser = get_parser()
        text = parser.parse(serializer.validated_data['document'].read())
        logging.error(text)
        return Response(status=status.HTTP_201_CREATED)
