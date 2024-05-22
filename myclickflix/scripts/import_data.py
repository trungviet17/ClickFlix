import pandas as pd
from tqdm import tqdm
import os
from main.models import Actor, Category, Movie

FOLDER_PATH = os.path.join("..", "Data")


def run_category():
    category_df = pd.read_pickle(os.path.join(FOLDER_PATH, "genres.pkl"))
    for _, row in tqdm(category_df.iterrows(), total=category_df.shape[0]):
        if not Category.objects.filter(pk=row["id"]).exists():
            category = Category(pk=row["id"], name=row["genre"])
            category.save()
    print("Import category data done!")


def run_actor():
    actor_df = pd.read_pickle(os.path.join(FOLDER_PATH, "actors.pkl"))
    for _, row in tqdm(actor_df.iterrows(), total=actor_df.shape[0]):
        if not Actor.objects.filter(pk=row["id"]).exists():
            actor = Actor(
                name=row["name"],
                birthday=row["birthday"],
                bio=row["bio"],
                image=row["image"],
                pk=row["id"],
            )
            actor.save()
    print("Import actor data done!")


def run_movie():
    movie_df = pd.read_pickle(os.path.join(FOLDER_PATH, "movies.pkl"))
    for _, row in tqdm(movie_df.iterrows(), total=movie_df.shape[0]):
        if not Movie.objects.filter(pk=row["TMDB_id"]).exists():
            movie = Movie(
                title=row["Title"],
                score=row["score"],
                popularity=row["popularity"],
                overview=row["overview"],
                language=row["language"],
                released=row["released"],
                image=row["image"],
                price=2,
                pk=row["TMDB_id"],
            )
            movie.set_keyword(row["keyword"])
            movie.save()

            categories = Category.objects.filter(id__in=row["genre"])
            movie.categories.set(categories)

            actors = Actor.objects.filter(id__in=row["casts"])
            movie.actors.set(actors)
    print("Import movie data done!")


def run():
    run_actor()
    run_category()
    run_movie()
