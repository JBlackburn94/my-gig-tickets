from myvenue import db


class Event_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    venue_name = db.Column(db.String, nullable=False)
    city_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "#{0} - Event {1} | Venue: {2} | City: {3}".format(
            self.id, self.event_name, self.venue_name, self.city_name,
        )

