test_list = list(map(int, input().split()))

bigger_list = []

for i in range(1, len(test_list)):
    if test_list[i] > test_list[i - 1]:
        bigger_list.append(test_list[i])
print(*bigger_list)