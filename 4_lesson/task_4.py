n = int(input())
fact = 1
sum_of_facts = 0
for i in range(1, n + 1):
    fact *= i
    sum_of_facts += fact
print(sum_of_facts)
