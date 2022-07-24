import logging


class Config:
    DEBUG = False
    DEVELOPMENT = False
    LOCALHOST = False
    LOG_LEVEL = logging.INFO
    APP_NAME = 'simple-tracking'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass


class TestConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    LOCALHOST = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG


class LocalConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    LOCALHOST = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/simple_tracking'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG
