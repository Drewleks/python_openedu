dct = {}
l = []


def parse(L):
    country = L[:L.find(' ')]
    citiess = L[L.find(' ')+1:]
    cities = citiess.split()
    return (country, cities)


for i in range(int(input())):
    L = input()
    country, cities = parse(L)
    for city in cities:
        if city not in dct:
            dct[city] = []
        dct[city].append(country)
for i in range(int(input())):
    s = input()
    print(''.join(dct[s]))
