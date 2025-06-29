import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://postgres:HXzmecFtgqliKiOuoERouvowaugSpHRp@shortline.proxy.rlwy.net:40531/railway', 'postgresql://user:pass@localhost:5432/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
