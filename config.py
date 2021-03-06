import os

class Config:
    '''
    configration of the parent class
    '''
    SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_option = {
    'development':DevConfig,
    'production':ProdConfig
    }
