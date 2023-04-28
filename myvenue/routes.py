from flask import render_template, request, redirect, url_for
from myvenue import app, db
from myvenue.models import Event_Details


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/my_events")
def my_events():
    return render_template("my_events.html")


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event = Event_Details(event_name=request.args.get("event_name"))
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("my_events"))
    return render_template("add_event.html")
