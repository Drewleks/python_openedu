a = int(input())
max_num = 0
while a != 0:
    if a > max_num:
        max_num = a
        a = int(input())
    else:
        a = int(input())
print(max_num)
