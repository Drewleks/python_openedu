fout=open('task7-1-3.html','w')
s=['<html>\n','<body>\n','<table>\n']
fout.writelines(s)
s=[]
for i in range (1,11):
    s.append('<tr>\n')
    for j in range(1,11):
        s.append('<td><a href=\'http://'+str(i*j)+'.ru\'>'+str(i*j)+'</a></td>\n')
    s.append('</tr>\n')
s.append('</table>\n</body>\n</html>')
fout.writelines(s)
fout.close()