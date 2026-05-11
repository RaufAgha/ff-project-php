from django.db import models
from categories.models import Category

class Transaction(models.Model):
    TYPES = [('income','Income'),('expense','Expense')]
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.type})"