def test_orderline_mapper_can_load_movies(session):  # (1)
    session.execute(
        "INSERT INTO movies (preferenceKey,movieTitle,rating) VALUES "
        '(1, "El hoyo", 8.2),'
        '(2, "Terremoto", 4.1),'
        '(3, "Avengers", 9.4),'
    )
    expected = [
        model.Movie(1, "El hoyo", 8.2),
        model.Movie(2, "Terremoto", 4.1),
        model.Movie(3, "Avengers", 9.4),
    ]
    assert session.query(model.Movie).all() == expected


def test_orderline_mapper_can_save_movies(session):
    new_movie = model.Movie(1, "Midsomar", 6.3)
    session.add(new_movie)
    session.commit()

    rows = list(session.execute(
        'SELECT preferenceKey,movieTitle,rating FROM "movies"'))
    assert rows == [(1, "Midsomar", 6.3)]
