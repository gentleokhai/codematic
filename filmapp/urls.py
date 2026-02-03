from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


# the global URL patterns for the project
urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"), 
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include("film.urls")),
]
