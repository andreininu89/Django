from django.urls import path, include
from basic_app import views

# TEMPLATE_URLS
app_name = "basic_app"

urlpatterns = [
    path("register/", views.register, name="register"),
]
