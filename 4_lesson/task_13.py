test_list = list(map(int, input().split()))

index_of_max = test_list.index(max(test_list))
index_of_min = test_list.index(min(test_list))

test_list[index_of_max], test_list[index_of_min] = test_list[index_of_min], test_list[index_of_max]

print(*test_list)
