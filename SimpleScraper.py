import requests
from bs4 import BeautifulSoup

class SimpleScraper():
    url = ""

    def request_fn(self):
        try :
            return requests.get(self.url).content
        except:
            print("Invalid")

    def parse_fn(self, html_text):
        return BeautifulSoup(html_text, "html.parser")

    def find_fn(self, html_parse, tag, attribute = None):
        if attribute == None:
            return html_parse.find_all(tag[0])
        if attribute != None:
            html_list =  []
            for i in html_parse.find_all(tag[0]):
                if i.has_attr(attribute):
                    html_list.append(i)
            return html_list
