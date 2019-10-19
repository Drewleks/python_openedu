N = int(input())
lst = []

while len(lst) != N:
    lst.append(input())
    lst.sort()
print(*lst, sep='\n')