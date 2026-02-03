from django.urls import path
from film.views import FilmListView, CommentListCreateView

urlpatterns = [
    path("films/", FilmListView.as_view()),
    path("films/<int:film_id>/comments/", CommentListCreateView.as_view()),
]
