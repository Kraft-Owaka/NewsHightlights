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
    sports_news=get_source('sports')
    return render_template('index.html', title = title,entertainment=general_news,business=business_news,sports_news)

    @main.route('/article/<id>')
    def article(id):
        article = get_articles(id)
        print(***get_article***)
        print(article)
        title='ARTICLES'
        return render_template('article.html',title = title,id=id,article=article)