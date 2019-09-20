s = input()
if s.startswith('+'):
    print(s)
elif s.startswith('8'):
    print(s.replace('8', '+7', 1))
elif len(s) == 9:
    print('+7' + s)
