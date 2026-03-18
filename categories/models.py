from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=10,choices=[('income','Income'),('expense','Expense')])
    color=models.CharField(max_length=7, default='#000000')
    icon=models.CharField(max_length=50,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return f"{self.name} ({self.type})"