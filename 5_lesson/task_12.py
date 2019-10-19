l = list(input().split())
l_max = {}

for el in l:
    l_max[el] = l_max.get(el, 0) + 1

itemMaxValue = max(l_max.items(), key=lambda x: x[1])

listOfKeys = list()

for key, value in l_max.items():
    if value == itemMaxValue[1]:
        listOfKeys.append(key)
print(min(listOfKeys))