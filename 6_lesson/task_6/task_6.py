fin = open('input.txt', 'r', encoding='utf8')
s = fin.readlines()

max_len = 0
max_len_list = []

for el in range(len(s)):
    if len(s[el]) > max_len:
        max_len = len(s[el])
        max_len_list = s[el]

print(max_len_list)
