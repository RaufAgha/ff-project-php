from django.shortcuts import render
from django.http import HttpResponse

# Minimal view funksiyası
def category_list(request):
    return HttpResponse("Categories")