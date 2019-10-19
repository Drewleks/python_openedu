fin = open('input.txt', 'r', encoding='utf8')

sum_of_line = []

for line in fin:
    sum_of_line.append(sum(map(int, line.split())))
fin.close()

print(*sum_of_line)
