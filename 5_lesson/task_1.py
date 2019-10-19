N = int(input())
lst = []

while len(lst) != N:
    lst = list(map(int, input().split()))
    lst.sort()
print(*lst)
