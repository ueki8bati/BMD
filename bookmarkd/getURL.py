import urllib.request
from bs4 import BeautifulSoup

def get_url(url):
    r =  urllib.request.urlopen(url)
    html = r.read()
    soup = BeautifulSoup(html,'html.parser')
    t = soup.get_text()
    return t 