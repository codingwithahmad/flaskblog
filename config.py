import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_PORT= os.getenv('MAIL_PORT')
    MAIL_USE_TLS= os.getenv('MAIL_USE_TLS')


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False
