import os

class Config():

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Jacques@localhost/minute'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True

config_options={
'production':ProdConfig,
'development':DevConfig
}
