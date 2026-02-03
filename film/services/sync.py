from .swapi import fetch_films
from film.models import Film

def sync_films():
    films = fetch_films()
    for film in films:
        Film.objects.update_or_create(
            swapi_id=film["swapi_id"],
            defaults={
                "title": film["title"],
                "release_date": film["release_date"],
            }
        )
