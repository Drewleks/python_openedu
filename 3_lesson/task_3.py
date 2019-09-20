x = float(input())

if x % 1 == 0.0:
    print(0)
else:
    x = round(x - int(x), 3)
    print(abs(x))

