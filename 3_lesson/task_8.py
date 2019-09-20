s = input()
subs = 'f'
if s.count(subs) > 1:
    print(s.find(subs), s.rfind(subs))
elif s.count(subs) == 1:
    print(s.find(subs))
