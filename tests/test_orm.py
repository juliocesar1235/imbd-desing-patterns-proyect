import models


def test_mapper_can_load_movies(session):  # (1)
    session.execute(
        "INSERT INTO movies (preferenceKey,movieTitle,rating,year,place,vote,link) VALUES "
        '(1,"Sueño de fuga,Frank Darabont (dir.), Tim Robbins, Morgan Freeman",9.239903039104593,1994,1,NULL,"/title/tt0111161/"),'
        '(4,"El padrino II,Francis Ford Coppola (dir.), Al Pacino, Robert De Niro",8.99012508760967,1974,4,NULL,"/title/tt0071562/"),'
    )
    expected = [
        models.Movie(1, "Sueño de fuga,Frank Darabont (dir.), Tim Robbins, Morgan Freeman",
                     9.239903039104593, 1994, 1, NULL, "/title/tt0111161/"),
        models.Movie(4, "El padrino II,Francis Ford Coppola (dir.), Al Pacino, Robert De Niro",
                     8.99012508760967, 1974, 4, NULL, "/title/tt0071562/"),
    ]
    assert session.query(models).all() == expected


def test_mapper_can_save_movies(session):
    new_movie = models.Movie(1, "El origen,Christopher Nolan (dir.), Leonardo DiCaprio, Joseph Gordon-Levitt",
                             8.743839456695438, 2010, 13, NULL, "/title/tt1375666/")
    session.add(new_movie)
    session.commit()

    rows = list(session.execute(
        'SELECT preferenceKey,movieTitle,rating FROM "movies"'))
    assert rows == [(1, "El origen,Christopher Nolan (dir.), Leonardo DiCaprio, Joseph Gordon-Levitt",
                     8.743839456695438)]
