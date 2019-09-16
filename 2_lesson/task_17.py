first = int(input())

max_value = first
max_cnt = 1

while first != 0:
    if max_value == first:
        max_cnt += 1
    elif max_value < first:
        max_value = first
        max_cnt = 1
    first = int(input())
print(max_cnt)
