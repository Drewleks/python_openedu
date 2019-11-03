fin=open('input.csv','r',encoding='utf8')
d=dict()
l=[]
for line in fin:
    s=line.split(';')
    if not s[0] in d:
        d[s[0]]=[int(s[1]),1]
    else:
        d[s[0]]=[d[s[0]][0]+int(s[1]),d[s[0]][1]+1]
fin.close()
for k,v in sorted(d.items(),key=lambda x: x[0]):
    l.append([k,v[0]//v[1]])#делим нацело, хз зачем, можно и обычное деление
for i in sorted(l,key=lambda x: (x[1],x[0])):
    print(i[0])#выводим только названия