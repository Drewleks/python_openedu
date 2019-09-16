a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = c * a * 2 + c * b * 2
total_rolls = abs(-s // d)
print(total_rolls)
