from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String, nullable = False)
    description = db.Column(db.String(250), nullable = False)
    adress = db.Column(db.String(250), nullable = False)
    total_seats = db.Column(db.Integer, nullable = False)
    free_seats = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return (f'name={self.name}, email={self.email}, password={self.password}. '
                f'description={self.description}, adress={self.adress}, total_seats={self.total_seats})')
