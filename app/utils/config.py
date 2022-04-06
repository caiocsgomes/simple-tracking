import logging


class Config:
    DEBUG = False
    DEVELOPMENT = False
    LOG_LEVEL = logging.INFO
    APP_NAME = 'simple-tracking'


class ProdConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG
