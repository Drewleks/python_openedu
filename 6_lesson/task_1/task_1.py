fin = open('input.txt', 'r', encoding='utf8')

word_count = 0

for line in fin:
    word_count += len(set(line.split()))
fin.close()

print(word_count)
