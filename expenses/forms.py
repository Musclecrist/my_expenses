from django import forms
from .models import Expense


# creating a form
class ExpenseForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Expense

        # specify fields to be used
        fields = [
            "store",
            "day",
            "sum",
            "product"
        ]

class CalculateForm(forms.Form):
    CHOICES = (('1', 'January'),('2', 'February'),('4','April'),('12','December'))
    month = forms.ChoiceField(choices=CHOICES)