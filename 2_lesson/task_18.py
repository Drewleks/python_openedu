num_cnt = int(input())

fact = 0
zero_count = 0

while fact != num_cnt:
    num = int(input())
    if num == 0:
        zero_count += 1
    fact += 1
print(zero_count)

