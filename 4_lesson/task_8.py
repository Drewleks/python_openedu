test_list = list(map(int, input().split()))

for i in range(0, len(test_list)):
    if test_list[i] % 2 == 0:
        print(test_list[i], end=' ')
