x = int(input())
y = int(input())
z = int(input())


def sort3(a, b, c):
    l = [a, b, c]
    print(*sorted(l))


sort3(x, y, z)
