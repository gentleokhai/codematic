from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Count
from film.models import Film, Comment
from film.serializers import FilmSerializer, CommentSerializer
from film.services.sync import sync_films
from rest_framework import generics, filters



class FilmListView(generics.ListAPIView):
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        sync_films()
        return (
            Film.objects
            .annotate(comment_count=Count("comments"))
            .order_by("release_date")
        )


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            film_id=self.kwargs["film_id"]
        )

    def perform_create(self, serializer):
        film = generics.get_object_or_404(
            Film, id=self.kwargs["film_id"]
        )
        serializer.save(film=film)
