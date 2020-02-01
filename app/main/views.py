from flask import render_template
from app import app

# Views
@main.route('/') #is a route decorator
def index(): # function

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')