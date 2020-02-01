from flask import Flask
from .config import config_options


# Initializing application
app = Flask(__name__,instance_relative_config = True)

#setting up configuration 
from.request import configure_request
configure_request(app)

return app