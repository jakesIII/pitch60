import os

class Config():

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Jacques@localhost/minute'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True

config_options={
'production':ProdConfig,
'development':DevConfig
}
