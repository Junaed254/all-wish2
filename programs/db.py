import requests
from config import API_KEY


def update_views(anime):
    try:
        requests.get(
            f"http://anikatsu.shashanktiwar11.repl.co{API_KEY}&anime={anime.strip()}"
        )
    except Exception as e:
        print(e)
    return


def update_watch(anime):
    try:
        requests.get(
            f"http://anikatsu.shashanktiwar11.repl.co/db/watch?key={API_KEY}&anime={anime.strip()}"
        )
    except Exception as e:
        print(e)
    return
