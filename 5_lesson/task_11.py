l = list(input().split())
l_max = {}
l_list = []

for el in l:
    if el not in l_max.keys():
        l_max[el] = l_max.get(el, 0)
        l_list.append(0)
    else:
        l_max[el] = l_max.get(el, 0) + 1
        l_list.append(l_max[el])

print(*l_list)
