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


@app.route("/delete_artist/<int:artist_id>")
def delete_artist(artist_id):
    art = Artist.query.get_or_404(artist_id)
    db.session.delete(art)
    db.session.commit()
    return redirect(url_for("my_events"))


@app.route("/event_list")
def event_list():
    events = list(Events.query.order_by(Events.id).all())
    return render_template("event_list.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    events = list(Artist.query.order_by(Artist.artist_name).all())
    if request.method == "POST":
        event = Events(
            event_name=request.form.get("event_name"),
            venue_name=request.form.get("venue_name"),
            city_name=request.form.get("city_name"),
            date=request.form.get("date"),
            event_id=request.form.get("event_id")
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("event_list"))
    return render_template("add_event.html", events=events)


@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = Events.query.get_or_404(event_id)
    events = list(Artist.query.order_by(Artist.artist_name).all())
    if request.method == "POST":
        event.event_name = request.form.get("event_name")
        event.venue_name = request.form.get("venue_name")
        event.city_name = request.form.get("city_name")
        event.date = request.form.get("date")
        event.event_id = request.form.get("event_id")
        db.session.commit()
        return redirect(url_for("event_list"))
    return render_template("edit_event.html", event=event, events=events)


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    event = Events.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for("event_list"))