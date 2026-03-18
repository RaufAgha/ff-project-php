from django.shortcuts import render
from django.http import HttpResponse

def transaction_list(request):
    return HttpResponse("Transactions")