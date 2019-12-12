a = open('1.html', 'r', encoding='utf8')
cnt_python = 0
cnt_cpp = 0
for line in a:
    cnt_python += line.count('Python')
    cnt_cpp += line.count('C++')
print('Python') if cnt_cpp < cnt_python else print('C++')
a.close()
