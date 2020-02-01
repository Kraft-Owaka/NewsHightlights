from flask import Flask
from .config import config_options


# Initializing application
app = Flask(__name__)

#setting up configuration 
app.config.from_object(DevConfig)

from app import views