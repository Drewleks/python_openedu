s = {}

for i in range(int(input())):
    key, value = input().split()
    s[key] = value
target_word = input()
l = list(s.items())


for i in range(len(l)):
    if target_word in l[i]:
        if l[i].index(target_word) == 0:
            print(l[i][1])
        else:
            print(l[i][0])
