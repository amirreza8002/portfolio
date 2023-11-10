from django.urls import path

from .views import HomeView, about

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", about, name="about"),
]
