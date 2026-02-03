import requests
from datetime import datetime

SWAPI_FILMS_URL = "https://swapi.dev/api/films/"

def fetch_films():
    response = requests.get(SWAPI_FILMS_URL, timeout=10)
    response.raise_for_status()

    films = []
    for film in response.json()["results"]:
        films.append({
            "swapi_id": int(film["url"].rstrip("/").split("/")[-1]),
            "title": film["title"],
            "release_date": datetime.strptime(
                film["release_date"], "%Y-%m-%d"
            ).date(),
        })
    return films
