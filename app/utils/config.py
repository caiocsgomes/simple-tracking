class Config:
    DEBUG = False
    DEVELOPMENT = False


class ProdConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQL_ALCHEMY_DATABASE_URI = 'sqlite:///site.db'
