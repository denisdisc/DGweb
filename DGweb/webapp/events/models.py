from webapp.db import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Event {} {}>'.format(self.title, self.url)
 