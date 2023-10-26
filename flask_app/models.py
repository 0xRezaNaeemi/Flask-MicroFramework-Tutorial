from flask_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return self.name
    
class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    writer_id = db.Column(db.Integer(), db.ForeignKey("writer.id"))
    writer = db.relationship("Writer", backref = db.backref("books"))

# use one time when creating a database
# with app.app_context():
#     db.create_all()