x = int(input())

for i in range(10 ** x - 1, 10 ** (x - 1) - 1, -2):
    print(i, end=' ')
