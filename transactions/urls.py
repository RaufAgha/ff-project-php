from django.urls import path
from .views import (
    transaction_list,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView   
)

urlpatterns = [
    path('', transaction_list, name='transaction_list'),
    path('add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('edit/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_edit'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'), 
]