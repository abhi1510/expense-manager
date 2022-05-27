from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Transaction
from .forms import TransactionForm


class TransactionListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/sign-in/'
    template_name = 'transactions/tran-list.html'

    def get_queryset(self):
        return Transaction.objects.order_by('-transaction_date')


class TransactionCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/sign-in/'
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/tran-form.html'
    success_url = reverse_lazy('transaction-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TransactionCreateView, self).form_valid(form)
