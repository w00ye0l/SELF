from django.urls import path
from . import views

app_name = "TE"

urlpatterns = [
    path("", views.index, name="home"),
    path("wintext/", views.wintext, name="wintext"),
    path("about/", views.about, name="about"),
    path("get_text/", views.get_text, name="get_text"),
    path('bookfind/', views.bookfind, name='bookfind'),
    path('voice/', views.voice, name='voice'),
]