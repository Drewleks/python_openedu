L = []
M = set()
for i in range(int(input())):
    for j in range(int(input())):
        M.add(input())
    L.append(M.copy())
    M.clear()

M = L[0]
U = M.copy()
for X in L[1:]:
    M &= X  # intersection
    U |= X  # union

print(len(M), *sorted(M), len(U), *sorted(U), sep='\n')
