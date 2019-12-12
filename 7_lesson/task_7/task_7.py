from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url="https://stepik.org/media/attachments/lesson/258939/webpage.html"

response = urlopen(url)
html = response.read().decode('utf-8')
soup = bs(html, 'lxml')
for link in soup.find_all('a'):
    if link.has_attr('href'):
        print(link.get('href'))
