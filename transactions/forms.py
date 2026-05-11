from django import forms
from .models import Transaction
from categories.models import Category


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'type', 'category', 'date', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        # DEBUG (istəsən görmək üçün)
        # print(self.data)

        # CREATE zamanı (POST gələndə)
        if self.data.get('type'):
            t_type = self.data.get('type')

            self.fields['category'].queryset = Category.objects.filter(
                type=t_type
            )

        # UPDATE zamanı (instance varsa)
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(
                type=self.instance.type
            )