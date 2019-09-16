a = int(input())
count = 0
square = 1
while square <= a:
    print(2 ** count, end=' ')
    count += 1
    square = 2 ** count
