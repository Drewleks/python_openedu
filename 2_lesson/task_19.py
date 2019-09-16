num = int(input())
cnt = 1
sec_cnt = 1
while sec_cnt != num + 1:
    cnt = 1
    while cnt != sec_cnt + 1:
        print(cnt, end='')
        cnt += 1
    print()
    sec_cnt += 1
