from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns = [
    path("relative/", views.relative, name="relative_url_templates"),
    path("base/", views.base, name="base"),
    path("other/", views.other, name="other"),
]
