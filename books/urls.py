from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("correct/", views.correct, name="correct"),
    path("incorrect/", views.incorrect, name="incorrect"),
]
