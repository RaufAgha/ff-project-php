from django.urls import path
from .views import (
    category_list,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView
)

urlpatterns = [
    path('', category_list, name='category_list'),

    path('add/', CategoryCreateView.as_view(), name='category_add'),

    path('edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),

    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]