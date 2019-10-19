numbers = list(map(int, input().split()))
numbers_set = set()

for num in numbers:
    if num not in numbers_set:
        numbers_set.add(num)
        print('NO')
    elif num in numbers_set:
        print('YES')
