fin = open('input.csv', 'r', encoding='utf8')

for line in fin:
    now = line.split(';')
    print(now)
print(now)
print(len(now))
