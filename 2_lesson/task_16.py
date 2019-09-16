first = int(input())
temp = first

cnt = 0

while first != 0:
    if temp < first:
        temp = first
        cnt += 1
    else:
        temp = first
    first = int(input())
print(cnt)
