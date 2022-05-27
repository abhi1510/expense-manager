from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignUpView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(template_name='accounts/sign-in.html'), name='sign-in'),
    path('sign-out', LogoutView.as_view(), name='sign-out'),
]
