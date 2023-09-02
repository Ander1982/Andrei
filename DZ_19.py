
import os

# objs = os.listdir('pop')
#
# files = []
# dirs = []
#
# for i in objs:
#     f_1 = os.path.join('pop', i)
#
#     if os.path.isfile(f_1):
#         files.append(f_1)
#     else:
#         dirs.append(f_1)
#
# f_3 = files + dirs
# print(f_3)
#
objs = os.listdir('pop')

j = []

for i in objs:
    f_1 = os.path.join('pop', i)

    j.append(f_1)

# j_2 = sorted(j, key=os.path.isfile, reverse=True)
# print(j_2)

j.sort(key=os.path.isfile, reverse=True)
print(j)