from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_articles
from ..model import Source

# Views
@main.route('/') #is a route decorator
def index(): # view function

    '''
    View root page function that returns the index page and its data
    ''' 
    general_news = get_source('entertainment')
    print('*-*-*Stories*-*-*')
    print(general_news)
    business_news=get_source('business')
    return render_template('index.html')