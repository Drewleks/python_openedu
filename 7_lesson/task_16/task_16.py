url="https://stepik.org/media/attachments/lesson/209723/5.html"
#url='input16.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
#soup=BS(html,'html5lib') #Парсер html5ib не поможет
soup=BS(html,'lxml')
sum=0
pTag=soup.find('table')
for i in pTag.findAllNext(text=True):
    i.strip()

    if i!='\n':
        sum+=int(i)
print(sum)#28734