url="https://stepik.org/media/attachments/lesson/258944/New-York.html"
#url='New-York.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

fout=open('out18.csv','w',encoding='utf8')

table= soup.find_all('table',attrs={"class": "wikitable collapsible collapsed"})[1]
#Пишем th
print(table.find('th').text.strip(),file=fout)
rows=table.find_all('tr')
for row in rows:
    tds=row.find_all('td')
    str1=''
    for td in tds:
        #print(td)
        str1+=td.text+","

    print(str1[:-1],file=fout,end='')
print(file=fout)
fout.close()