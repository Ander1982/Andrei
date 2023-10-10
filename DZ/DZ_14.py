
s = 'I am learning Python. hello, WORD!'
slice_1 = s[s.index("h"):s.rindex("h"):]
slice_2 = slice_1[::-1]
s1 = s[:s.find('h') + 1:] + slice_2 + s[s.rfind('h') + 1:]
print(s1)

s = 'I am learning Python. hello, WORD!'
s1 = s[:s.find('h') + 1:] + s[s.index("h"):s.rindex("h")][::-1] + s[s.rfind('h') + 1:]
print(s1)