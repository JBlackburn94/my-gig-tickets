from flask import render_template, request, redirect, url_for
from myvenue import app, db
from myvenue.models import Artist, Events


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/my_events")
def my_events():
    events = list(Artist.query.order_by(Artist.artist_name).all())
    return render_template("my_events.html", artist=events)


@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    if request.method == "POST":
        artist = Artist(artist_name=request.form.get("artist_name"))
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for("my_events"))
    return render_template("add_artist.html")


@app.route("/edit_artist/<int:artist_id>", methods=["GET", "POST"])
def edit_artist(artist_id):
    art = Artist.query.get_or_404(artist_id)
    if request.method == "POST":
        art.artist_name = request.form.get("artist_name")
        db.session.commit()
        return redirect(url_for("my_events"))
    return render_template("edit_artist.html", art=art)
