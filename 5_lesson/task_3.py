def mykey(x):
    return x[1]


N = int(input())
lst = []
outer_list = []


for i in range(N):
    lst = list(input().split())
    outer_list.append(lst)
outer_list.sort(key=mykey)

for el in outer_list:
    print(*el)


