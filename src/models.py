from __future__ import annotations
from datetime import datetime
import os

from dataclasses import dataclass
from sqlalchemy import create_engine


class Movie:
    preference_key = int
    movie_title = str
    rating = float
    year = int
    place = int
    vote = int
    link = str
    create_time: datetime | None = None

    def __init__(
        self,
        preference_key: int,
        movie_title: str,
        rating: float,
        year: int,
        place: int,
        vote: int,
        link: str,
    ):
        self.preference_key = preference_key
        self.movie_title = movie_title
        self.rating = rating
        self.year = year
        self.place = place
        self.vote = vote
        self.link = link
