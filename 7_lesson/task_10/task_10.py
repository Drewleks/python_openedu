def getlinks(url):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    soup = BS(html, 'lxml')

    links=[]#надо все ссылки

    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                links.append(s)
    return links

url="https://stepik.org/media/attachments/lesson/258943/Moscow.html"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

links=getlinks(url)
print(len(links))