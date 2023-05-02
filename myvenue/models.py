from myvenue import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), unique=True, nullable=False)
    event = db.relationship("Events", backref="artist", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.artist_name


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    venue_name = db.Column(db.String, nullable=False)
    city_name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("artist.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Event: {1} | Venue: {2} | City: {3} | Date: {4}".format(
            self.id, self.event_name, self.venue_name, self.city_name, self.date
        )