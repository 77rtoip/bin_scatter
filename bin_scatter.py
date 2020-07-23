import numpy as np
import matplotlib.pyplot as plt

def diff_by_one(s1, s2):
    if len(s1)!=len(s2): return False
    return sum(c1!=c2 for c1, c2 in zip(s1, s2)) == 1

def nbin(n, digits):
    return bin[2:].zfill(digits)

number = 4

limit = 2**number

x = []
y = []

for i in range(limit):
    for j in range(limit):
        if diff_by_one(bin(i), bin(j)):
            x.append(i)
            y.append(j)


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(x, y, color='b', marker = 's')
plt.show()
