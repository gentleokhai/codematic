from django.core.cache import cache
from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from film.models import Film, Comment
from film.serializers import FilmSerializer, CommentSerializer


CACHE_TIMEOUT = 60 * 5  # 5 minutes

class FilmListView(generics.ListAPIView):
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        search = self.request.query_params.get("search", "")
        cache_key = f"films:list:search={search}"

        # Try to get from cache
        films = cache.get(cache_key)
        if films is None:
            # Query DB if not cached
            qs = Film.objects.annotate(comment_count=Count("comments")).order_by("release_date")
            if search:
                qs = qs.filter(title__icontains=search)

            films = FilmSerializer(qs, many=True).data
            cache.set(cache_key, films, CACHE_TIMEOUT)
        return films


class CommentCreateThrottle(UserRateThrottle):
    rate = "20/hour"  # max 20 comments per user per hour

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    throttle_classes = [CommentCreateThrottle]


    def get_queryset(self):
        return Comment.objects.filter(film_id=self.kwargs["film_id"])

    def perform_create(self, serializer):
        film = get_object_or_404(Film, id=self.kwargs["film_id"])
        serializer.save(film=film)

        # Invalidate ALL film list caches
        keys = cache.keys("films:list:*")  # works with Redis backend
        if keys:
            cache.delete_many(keys)
