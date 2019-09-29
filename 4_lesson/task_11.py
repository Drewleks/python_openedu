test_list = list(map(int, input().split()))

new_list = []
count = 0


for i in range(1, len(test_list) - 1):
    if test_list[i - 1] < test_list[i] > test_list[i + 1]:
        count += 1
print(count)
