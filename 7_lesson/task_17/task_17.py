url="https://stepik.org/media/attachments/lesson/258944/New-York.html"
#url='New-York.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

fout=open('out17.txt','w',encoding='utf8')

table= soup.find_all('table',attrs={"class": "wikitable collapsible collapsed"})[1]

print(table,file=fout)

fout.close()