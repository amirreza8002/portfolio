from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from allauth.account.views import PasswordChangeView


class LoggedOut(LogoutView):
    template_name = "account/logged_out.html"


class PasswordChangeDone(TemplateView):
    template_name = "account/password_change_done.html"


class PasswordChangeViewCustom(PasswordChangeView):
    success_url = reverse_lazy("change_password_done")
