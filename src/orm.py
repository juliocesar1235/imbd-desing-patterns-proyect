from sqlalchemy import Table, MetaData, Column, Integer, String, Float
from sqlalchemy.orm import mapper

import models  # (1)

metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("movie_id", Integer, primary_key=True, autoincrement=True),
    Column("preference_key", Integer),
    Column("movie_title", String(255)),
    Column("rating", Float(13)),
    Column("year", Integer),
    Column("place", Integer),
    Column("vote", Integer),
    Column("link", String(255)),
)


def start_mappers():
    mapper(models.Movie, movies)
