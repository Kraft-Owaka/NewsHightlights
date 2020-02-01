import unittest
from app.model import Article

class Article(unittest.TestCase):
    '''
    testing the movie class behaviour
    '''
def setUp(self):
    '''
    The set up method will run just before the test
    '''
    self.new_article = Article()

def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Article))

