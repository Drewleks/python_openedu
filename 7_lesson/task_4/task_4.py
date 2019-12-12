from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

response = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')
html = response.read().decode('utf-8')
soup = bs(html)
print(soup)
