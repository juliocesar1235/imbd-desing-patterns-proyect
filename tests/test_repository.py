import models
import repository


def test_repository_can_save_a_batch(session):
    movie = models.Movie(2, "Atrapado sin salida,Milos Forman (dir.), Jack Nicholson, Louise Fletcher",
                         8.649661620685299, 1975)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(movie)  # (1)
    session.commit()  # (2)

    rows = session.execute(  # (3)
        'SELECT preference_key, movie_title, rating, year  FROM "movies"'
    )
    assert list(rows) == [(2, "Atrapado sin salida,Milos Forman (dir.), Jack Nicholson, Louise Fletcher",
                           8.649661620685299, 1975)]
