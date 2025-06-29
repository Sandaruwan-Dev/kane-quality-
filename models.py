from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    real_name = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    is_approved = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    good_garment_total = db.Column(db.Integer)
    defeat_total = db.Column(db.Integer)
    test1 = db.Column(db.Integer)
    # add test2 ... test10 as needed
    line_job_card1 = db.Column(db.Integer)
    line_job_card2 = db.Column(db.Integer)
    # up to line_job_card14
