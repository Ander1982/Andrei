import re
t = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
print(re.findall(r'[1-9_a-zа-я.-]*@[a-z.]*', t))
