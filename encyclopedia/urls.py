from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("404error/", views.notfound, name="404error"),
    path("409error/", views.notallowed, name="409error"),
    path("<str:title>", views.entry, name="entry"),
    path("newpage/", views.new_page, name="newpage"),
    path("randompage/", views.random_page, name="randompage"),
    path("search/", views.search, name="search"),
    path("edit/", views.edit, name="edit")
]
