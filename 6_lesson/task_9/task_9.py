fin=open('input.csv','r',encoding='utf8')
fout=open('out.txt','w',encoding='utf8')
for line in fin:
    s=line.split(';')
    print(f'{s[1].strip()};{s[0].strip()}',sep='',file=fout)#отправим в файл, так как много строк муторно потом в проверяющую форму на портал закидывать
fin.close()
fout.close()