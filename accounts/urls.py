from django.urls import path, include

from . import views

urlpatterns = [
    path(
        "password/change/",
        views.PasswordChangeViewCustom.as_view(),
        name="account_change_password",
    ),
    path(
        "password/change/done/",
        views.PasswordChangeDone.as_view(),
        name="change_password_done",
    ),
    path("", include("allauth.urls")),
    path("loggedout/", views.LoggedOut.as_view(), name="logged_out"),
]
