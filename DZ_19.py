
import os

objs = os.listdir('pop')

files = []
dirs = []

for i in objs:
    f_1 = os.path.join('pop', i)

    if os.path.isfile(f_1):
        files.append(f_1)
    else:
        dirs.append(f_1)

f_3 = files + dirs
print(f_3)

