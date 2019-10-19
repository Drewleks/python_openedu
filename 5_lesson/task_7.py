myset_1 = list(map(int, input().split()))
myset_2 = list(map(int, input().split()))
myset_1 = set(myset_1)
myset_2 = set(myset_2)
myset_3 = myset_1.intersection(myset_2)

print(*sorted(myset_3))
