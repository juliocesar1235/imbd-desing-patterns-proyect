from sqlite3 import Date
from sqlalchemy import Table, MetaData, Column, Integer, String, Float, create_engine
from sqlalchemy.orm import mapper, sessionmaker, Session

import models
import config


engine = create_engine(
    config.get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)
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


def start_mappers() -> Session:
    mapper(models.Movie, movies)
    metadata.create_all(engine)
    return sessionmaker(bind=engine)()
