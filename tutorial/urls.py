from django.contrib import admin
from django.urls import path

from example.views import (
    MovieListView,
    PostCreateView,
    PostEditView,
    GenreCreateView,
    GenreEditView,
    hello_name,
    hello_world,
)


urlpatterns = [
    path("hello/", hello_world, name="hello_world"),
    path("hello/<str:name>/", hello_name, name="hello_name"),
    path("admin/", admin.site.urls),
    path("movie_list_by_class_view/", MovieListView.as_view(), name="movie_list"),
    path("movie/add/", PostCreateView.as_view(), name="movie_add"),
    path("movie/edit/<int:pk>/", PostEditView.as_view(), name="movie_edit"),
    path("genre/add/", GenreCreateView.as_view(), name="genre_add"),
    path("genre/edit/<int:pk>/", GenreEditView.as_view(), name="genre_edit"),
]
