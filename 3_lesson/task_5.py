p = int(input())
x = int(input())
y = int(input())

cents = x * 100 + y

total_in_pennies = cents + cents * p / 100
total_in_rubles = total_in_pennies / 100

total_in_rubles = str(total_in_rubles)
total_in_rubles_list = total_in_rubles.split(sep='.')


rubles = int(total_in_rubles_list[0])
pennies = str(total_in_rubles_list[1])
pennies = int(pennies[:2])

print(rubles, pennies)
