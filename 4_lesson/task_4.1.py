import math

x = int(input())
fact = 0
for i in range(1, x + 1):
    fact += math.factorial(i)
print(fact)