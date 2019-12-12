url="https://stepik.org/media/attachments/lesson/258944/New-York.html"
#url='New-York.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

fout=open('out19.csv','w',encoding='utf8')

table= soup.find_all('table',attrs={"class": "wikitable collapsible collapsed"})
for i in range(0,3):

    rows=table[i].find_all('tr')
    for row in rows:
        tds=row.find_all(['th','td'])
        str1=''
        for td in tds:
            str1+=td.text.strip()+","

        print(str1[:-1],file=fout)
    print(file=fout)
fout.close()