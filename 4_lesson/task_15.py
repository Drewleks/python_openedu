x = float(input())
y = float(input())


def isPointInSquare(a, b):
    if abs(a) <= 1 and abs(b) <= 1:
        print('YES')
    else:
        print('NO')


isPointInSquare(x, y)
