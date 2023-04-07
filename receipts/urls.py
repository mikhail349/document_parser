from django.urls import path

from receipts.views import ReceiptAPIView

urlpatterns = [
    path('', ReceiptAPIView.as_view()),
]
