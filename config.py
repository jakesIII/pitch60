class Config():

    pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    pass

config_options={
'production'=ProdConfig,
'development'=DevConfig
}
