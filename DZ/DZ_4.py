
n = [6, 3, 0, 8, 2]
c = 0
j = 0
for i in range(len(n)):
    if n[i] == 0:
        continue
    c += n[i]
    if n[i] != 0:
        j +=1

c = c / j
print(c)
