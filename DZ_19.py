
import os

objs = os.listdir('pop')
print(objs)
for i in objs:
    f_1 = os.path.join('pop', i)
    print(f'{f_1}')