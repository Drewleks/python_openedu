a = int(input())
b = int(input())
c = int(input())

m = a
if b > m:
    m = b
if c > m:
    m = c
    if b > c:
        m = b
print(m)
