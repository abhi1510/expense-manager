from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of the expense'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount spend in INR.'}),
            'transaction_date': forms.DateInput(attrs={'type': 'date'})
        }

