from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.select_related('category').all()

    # filters
    t_type = request.GET.get('type')
    category = request.GET.get('category')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    search = request.GET.get('search')

    if t_type:
        transactions = transactions.filter(type=t_type)

    if category:
        transactions = transactions.filter(category_id=category)

    if date_from:
        transactions = transactions.filter(date__gte=date_from)

    if date_to:
        transactions = transactions.filter(date__lte=date_to)

    if search:
        transactions = transactions.filter(
            Q(title__icontains=search) |
            Q(notes__icontains=search)
        )

    return render(request, 'transactions/list.html', {
        'transactions': transactions
    })

class TransactionCreateView(CreateView):
    model=Transaction
    form_class=TransactionForm
    template_name='transactions/form.html'
    success_url=reverse_lazy('transaction_list')


class TransactionUpdateView(UpdateView):
    model=Transaction
    form_class=TransactionForm
    template_name='transactions/form.html'
    success_url=reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model=Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')