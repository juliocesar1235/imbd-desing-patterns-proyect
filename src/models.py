from __future__ import annotations
import os

from dataclasses import dataclass
from sqlalchemy import create_engine


@dataclass(unsafe_hash=True)
class Movie:
    preference_key = int
    movie_title = str
    rating = float
    year = int
    place = int
    vote = int
    link = str

    def __repr__(self):
        return f"<Movie {self.movietitle}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other.movietitle == self.movietitle

    def __hash__(self):
        return hash(self.movietitle)

    def __gt__(self, other):
        if self.movietitle is None:
            return False
        if other.movietitle is None:
            return True
        return self.movietitle > other.movietitle
