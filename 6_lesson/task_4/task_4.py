fin = open('input.txt', 'r', encoding='utf8')
s = fin.readlines()
print(*s[::-1], sep='')
