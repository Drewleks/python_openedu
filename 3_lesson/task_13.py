s = input()
start = s.find('h')
finish = s.rfind('h')
s_str = s[:start + 1]
f_str = s[finish:]
s = s[start + 1:finish].replace('h', 'H')
print(s_str + s + f_str)

