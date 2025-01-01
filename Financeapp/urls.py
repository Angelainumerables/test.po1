from django.urls import path
from .views import HomePageView, TransactionPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('transaction/', TransactionPageView.as_view(), name='transaction'),
]