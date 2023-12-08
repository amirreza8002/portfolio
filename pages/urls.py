from django.urls import path

from .views import home, about, RobotTxtView

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("robots.txt", RobotTxtView.as_view(content_type="text/plain"), name="robots"),
]
