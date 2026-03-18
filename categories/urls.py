from django.urls import path
from . import views  # Yalnız views import edin

urlpatterns = [
    path('', views.category_list, name='category_list'),
]