from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error/", views.error, name="error"),
    path("<str:title>", views.entry, name="entry"),
    path("newpage/", views.new_page, name="newpage"),
    path("randompage/", views.random_page, name="randompage"),
    path("search/", views.search, name="search")
]
