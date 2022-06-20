from flask import Flask, request, jsonify, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

import config
import orm
import models
from repository import MovieRepository


session = orm.start_mappers()

app = Flask(__name__, instance_relative_config=True)
movieRepo = MovieRepository(session)


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/create-movie", methods=["POST"])
def movie_endpoint():
    repo = movieRepo
    # print(request.json)
    moviek = models.Movie(
        preference_key=request.json["preference_key"],
        movie_title=request.json["movie_title"],
        rating=request.json["rating"],
        year=request.json["year"],
        place=request.json["place"],
        vote=request.json["vote"],
        link=request.json["link"],
    )
    #print(movie.__repr__, "model")
    newMovie = repo.create(moviek)
    return jsonify(newMovie.movie_title, newMovie.rating), 200


@ app.route("/recomendations", methods=["GET"])
def movie_recomendations_endpoint():
    preferenceKey = request.json["preference_key"]
    repo = movieRepo
    lm = repo.list()
    print(lm)
    return jsonify(lm), 200
