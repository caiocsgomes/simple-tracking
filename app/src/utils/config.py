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
    pass


class LocalConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/simple_tracking'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG
