from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime
from transactions.models import Transaction


def dashboard(request):
    now = datetime.now()

    monthly_transactions = Transaction.objects.filter(
        date__month=now.month,
        date__year=now.year
    )

    total_income = monthly_transactions.filter(
        category__type='income'
    ).aggregate(total=Sum('amount'))['total'] or 0

    total_expense = monthly_transactions.filter(
        category__type='expense'
    ).aggregate(total=Sum('amount'))['total'] or 0

    balance = total_income - total_expense

    recent_transactions = Transaction.objects.order_by('-date')[:5]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'recent_transactions': recent_transactions,
        'current_month': now,
    }

    return render(request, 'dashboard/dashboard.html', context)