a = int(input())
b = int(input())
c = int(input())

if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    print("NO")
elif (a % 2 == 1) and (b % 2 == 1) and (c % 2 == 1):
    print("NO")
else:
    print('YES')
