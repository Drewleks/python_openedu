url="https://stepik.org/media/attachments/lesson/209723/4.html"
#url='input15.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')
'''
links=[]
sum=0
for link in soup.find_all(['td','b','i']):
    #print(link,link.text.strip())
    links.append(int(link.text.strip()))
for i in links:
    sum+=i
print(sum)
'''
sum=0
pTag=soup.find('table')
for i in pTag.findAllNext(text=True):
    i.strip()

    if i!='\n':
        sum+=int(i)
print(sum)