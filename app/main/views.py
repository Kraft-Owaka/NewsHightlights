from flask import render_template,request,redirect,url_for
from .import  main
from ..request import get_source,get_articles
from ..model import Source

# Views
@main.route('/') #is a route decorator
def index(): # view function

    '''
    View root page function that returns the index page and its data
    ''' 
    general_news = get_source('general')
    print('*************general news*********************')
    print(general_news)
    sports_news = get_source('sports')
    business_news = get_source('business')
    technology_news = get_source('technology')
   
    title='Feeds'

    return render_template('index.html', title=title, general=general_news, sports=sports_news, business=business_news, technology=technology_news,)

@main.route('/article/<id>')
def article(id):
    article = get_articles(id)
    print('***get_article***')
    print(article)
    title='Article hub'
    return render_template('article.html',title = title,id=id,article=article)