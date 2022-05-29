from sqlalchemy.orm import mapper, relationship

import model  # (1)

metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("movieId", Integer, primary_key=True, autoincrement=True),
    Column("preferenceKey", Integer),
    Column("movieTitle", String(255)),
    Column("rating", Float),
    Column("createTime", TIMESTAMP(timezone=True), index=True),
)


def start_mappers():
    movies_mapper = mapper(model.movies, movies)
