from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        IN = 'IN', _('Income')
        EXP = 'EXP', _('Expense')

    class TransactionMode(models.TextChoices):
        ON = 'ON', _('Online')
        CA = 'CA', _('Cash')

    title = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=3, choices=TransactionType.choices, default=TransactionType.EXP)
    transaction_mode = models.CharField(max_length=2, choices=TransactionMode.choices, default=TransactionMode.ON)
    transaction_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('transaction-detail', args=[str(self.pk)])

    def get_transaction_type(self):
        return self.TransactionType[self.transaction_type].label

    def get_transaction_mode(self):
        return self.TransactionMode[self.transaction_mode].label

    @classmethod
    def total_income(cls):
        return sum([x.amount for x in cls.objects.filter(transaction_type=cls.TransactionType.IN)])

    @classmethod
    def total_expense(cls):
        return sum([x.amount for x in cls.objects.filter(transaction_type=cls.TransactionType.EXP)])
