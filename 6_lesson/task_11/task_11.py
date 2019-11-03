fin=open('input.csv','r',encoding='utf8')
goods=fin.readline().rstrip('\n').split(';')
l=[]
#print(shops)
for line in fin:
    s=line.rstrip('\n').split(';')
    shop=s[0]
    for i in range(1,len(s)):
        l.append([int(s[i]),goods[i],shop])
fin.close()
#for i in sorted(l,key=lambda x: (x[0],x[1],x[2]))[0]:
#    print(i)
for i in range(2):
    print(sorted(l,key=lambda x: (x[0],x[1],x[2]))[0][i+1])