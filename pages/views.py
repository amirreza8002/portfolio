from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


class RobotTxtView(TemplateView):
    template_name = "pages/robots.txt"
