minima_list=[]
fin=open('input.csv','r',encoding='utf8')
s=fin.readline()
for line in fin:
    s=line.split(';')
    l=[]
    for i in range(1,len(s)):
        l.append(int(s[i].strip()))#из каждой строки берем все, кроме первого элемента, ищем минимальное
    minima_list.append(min(l))#добавляем в список минимальных
fin.close()
print(min(minima_list))#выводим самое минимальное из минимальных