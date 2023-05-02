from flask import render_template, request, redirect, url_for
from myvenue import app, db
from myvenue.models import Artist, Events


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/my_events")
def my_events():
    return render_template("my_events.html")


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    return render_template("add_artist.html")
