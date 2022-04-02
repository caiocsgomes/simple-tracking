from distutils.debug import DEBUG


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