from django.contrib import admin
from django.urls import path, include
from finance_tracker.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('transactions/', include('transactions.urls')),
    path('categories/', include('categories.urls')),
]