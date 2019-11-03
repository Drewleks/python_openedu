fin=open("input.txt",'r',encoding='utf8')

dct={}
lst=list()
for line in fin:
    s=line.split()
    lst+=s
    for word in s:
        if word in dct:
            dct[word]+=1
        else:
            dct[word]=1
fin.close()
file = open('out.txt','w')
#sorted_keys = sorted(dct, key=lambda x: int(dct[x]), reverse=True)
ss='''sorted_keys = sorted(dct, reverse=True)
dct1={}
for i in sorted_keys:
    s = str("{0};{1}\n").format(i, dct[i])
    file.writelines(s)
    dct1[dct[i]]=i
file.close()'''
lst=list()
for i in dct:
    lst.append([dct[i],i])
a=sorted(lst,reverse=True)#,key=lambda x: x[1])
b=sorted(a,key=lambda x: (-x[0],x[1]))
s=''
for i in b:
    #s = str("{0};{1}\n").format(i[0], i[1])
    s+=i[1]+' '
file.writelines(s)

file.close()