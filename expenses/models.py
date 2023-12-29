from django.db import models

# Create your models here.
class Expense(models.Model):
  store = models.CharField(max_length=255)
  day = models.DateTimeField()
  sum = models.DecimalField(max_digits=15, decimal_places=2)
  product = models.CharField(max_length=255)
