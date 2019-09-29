test_list = list(map(int, input().split()))

new_list = []


for i in range(len(test_list)):
    if test_list[i] > 0:
        new_list.append(test_list[i])
print(min(new_list))
