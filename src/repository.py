import abc
import models


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, movie: models.Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, movieTitle) -> models.Movie:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, movie):
        self.session.add(movie)

    def get(self, movieTitle):
        return self.session.query(models.Movie).filter_by(movieTitle=movieTitle).one()

    def list(self):
        return self.session.query(models.Movie).all()
