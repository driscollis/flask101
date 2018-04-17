from app import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        """"""
        self.name = name

    def __repr__(self):
        return "<Artist: {}>".format(self.name)


class Album(db.Model):
    """"""
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "albums", order_by=id), lazy=True)

    def __init__(self, title, release_date, publisher, media_type):
        """"""
        self.title = title
        self.release_date = release_date
        self.publisher = publisher
        self.media_type = media_type
