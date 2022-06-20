import abc
from sqlalchemy.orm import Session
import models


class AbstractRepository(abc.ABC):
    session: Session

    def __init__(self, session):
        self.session = session

    def add(self, movie: models.Movie):
        print(movie)
        self.session.add(movie)
        print(self.session)
        self.session.commit()

    @abc.abstractmethod
    def get(self, movieTitle) -> models.Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> list[models.Movie]:
        raise NotImplementedError


class MovieRepository(AbstractRepository):

    def create(self, movie) -> models.Movie:
        self.add(movie)
        return movie

    def get(self, movieTitle):
        return self.session.query(models.Movie).filter_by(movieTitle=movieTitle).one()

    def list(self) -> list[models.Movie]:
        return self.session.query(models.Movie).all()
