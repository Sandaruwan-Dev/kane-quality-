from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    real_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telephone = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    approved = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DailyReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, nullable=False)
    good_garment_total = db.Column(db.Integer)
    defeat_total = db.Column(db.Integer)
    line_job_card_1 = db.Column(db.Integer)
    line_job_card_2 = db.Column(db.Integer)
    test1 = db.Column(db.Integer)
    test2 = db.Column(db.Integer)
    test3 = db.Column(db.Integer)
    test4 = db.Column(db.Integer)
    test5 = db.Column(db.Integer)
    test6 = db.Column(db.Integer)
    test7 = db.Column(db.Integer)
    test8 = db.Column(db.Integer)
    test9 = db.Column(db.Integer)
    test10 = db.Column(db.Integer)
