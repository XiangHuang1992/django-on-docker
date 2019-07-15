from django.urls import path

from . import views


app_name = "upload"

urlpatterns = [path("", views.image_upload, name="image_upload")]
