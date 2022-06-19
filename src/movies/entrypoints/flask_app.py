from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

import config
import orm
import models
import repository as repository

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/create-movie", methods=["POST"])
def movie_endpoint():
    session = get_session()
    repo = repository.MovieRepository(session)
    movie = models.Movie(
        request.json["preferenceKey"],
        request.json["movieTitle"],
        request.json["rating"],
        request.json["year"],
        request.json["place"],
        request.json["vote"],
        request.json["link"],
    )
    repo.add(movie)
    response = {
        "movieTitle": movie.movietitle,
        "rating": movie.rating,
        "year": movie.year,
        "link": movie.link
    }
    return response, 200


@app.route("/recomendations", methods=["GET"])
def movie_recomendations_endpoint():
    session = get_session()
    repo = repository.MovieRepository(session)
    print(repo.list())
    return "recomendations", 200


orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
