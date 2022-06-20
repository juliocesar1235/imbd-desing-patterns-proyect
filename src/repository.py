import abc
from typing import Generic, TypeVar
from sqlalchemy.orm import Session
from models import Movie
import csv

T = TypeVar("T", Movie, None)


class AbstractRepository(abc.ABC, Generic[T]):
    session: Session

    def __init__(self, session):
        self.session = session

    def add(self, entity: T):
        self.session.add(entity)
        print(self.session)
        self.session.commit()

    @abc.abstractmethod
    def list(self) -> list[T]:
        raise NotImplementedError


class MovieRepository(AbstractRepository[Movie]):

    def create(self, movie: Movie) -> Movie:
        self.add(movie)
        return movie

    def get(self, movieTitle: str):
        return self.session.query(Movie).filter_by(movieTitle=movieTitle).one()

    def list(self) -> list[Movie]:
        return self.session.query(Movie).all()

    def seed(self):
        with open("/src/movies/movie_results.csv") as file:
            for row in csv.DictReader(file, skipinitialspace=True):
                self.add(Movie(
                    int(row["preference_key"]),
                    row["movie_title"],
                    float(row["rating"]),
                    int(row["year"]),
                    int(row["place"]),
                    0,
                    row["link"],
                )
                )
