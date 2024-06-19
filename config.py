class Config(object):
    DEBUG = False
    TESTING = False
    # Add other configuration variables

class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True