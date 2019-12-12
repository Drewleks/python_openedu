from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)
