q = int(input())
w = int(input())


def xor(a, b):
    if a and not b:
        print(1)
    elif b and not a:
        print(1)
    else:
        print(0)


xor(q, w)