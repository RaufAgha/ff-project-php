from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Count

from .models import Category

def category_list(request):
    categories = Category.objects.annotate(
        transaction_count=Count('transaction')
    )
    return render(request, 'categories/list.html', {'categories': categories})

class CategoryCreateView(CreateView):
    model=Category
    fields=['name','type']
    template_name='categories/form.html'
    success_url=reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model=Category
    fields=['name','type']
    template_name='categories/form.html'
    success_url=reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model=Category
    template_name='categories/category_confirm_delete.html'
    success_url=reverse_lazy('category_list')