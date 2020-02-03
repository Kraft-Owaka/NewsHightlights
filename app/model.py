class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,article_id,name,description,url,category,language,country,urlToImage):
        self.id=article_id
        self.name=name
        self.description = description
        self.url = url
        self.category=category
        self.language=language
        self.country=country
        self.urlToImage=urlToImage
class Article:

    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image= image
        self.date = date

## class Sources:
#     '''
#     Sources class defining Source Objects
#     '''
#     def __init__(self,name,description,source_url):
#         self.name = name
#         self.description = description
#         self.source_url = source_url