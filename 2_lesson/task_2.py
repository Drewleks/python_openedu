a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = int(input())

is_siesta = not c <= x <= d
is_open = a <= x <= b

print(is_siesta and is_open)
