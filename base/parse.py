from bs4 import BeautifulSoup


class HTMLDoc(object):
    """
    Base parse of HTML Doc
    """
    html_doc = BeautifulSoup

    def __init__(self, html_doc):
        self.html_doc = BeautifulSoup(html_doc, 'html.parser')




