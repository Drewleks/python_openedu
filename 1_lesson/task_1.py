x = 2112
i = 0
ans = 0
while i < x:
    ans += sum(map(lambda x: x ** 2, [i // 10, i % 13]))
    i += 7
print(ans)