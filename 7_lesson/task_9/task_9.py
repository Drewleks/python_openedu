url="https://stepik.org/media/attachments/lesson/209719/2.html"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')
'''
list_codes=[]
for link in soup.find_all('code'):
    if link.text not in list_codes:
        list_codes.append((str(link.text),1)
    list_codes[index(str(link.text))]+=1
for kk in sorted(list_codes,key=lambda k: k[1]):
    print(kk)
'''
links=[]
linkks=[]
#Сначала просто выдираем текст внутри тега в список (будут еще вложеннные теги, суп их игнорит
for link in soup.find_all('code'):
    links.append(link.text)
#Теперь делаем список списков - строка из списка 1 и количество повторений строки в списке 1
for i in sorted(links,reverse=True):
    linkks.append([i,links.count(i)])
#print(sorted(linkks,key=lambda k: (-k[1],k[0])))
#Ищем максимальное число повторений путем нехитрой сортировки
maxx=sorted(linkks,key=lambda k: (-k[1],k[0]))[0][1]
#Идем по списку списков, выбираем строки, количество повторов которых равно максимуму
set_max=[]
s_linkks=sorted(linkks,key=lambda k: (-k[1],k[0]))
for i in s_linkks:
    if i[1]==maxx:
        set_max.append(i[0])
print(*sorted(set(set_max)))