import random
import math
from re import U            
n = [random.randint(0,9) for i in range(7)]         # варинат 1, №1
print(n)

a = max(n)
print(a)

n.reverse()

print(n)

c = [random.randint(0,9) for y in range(10)]        # варинат 1, №2
print(c)

srznach = sum(c)/len(c)
print(srznach)

for q in range(len(c)):
    if c[q] == 0 :
        c[q] = srznach
print(c) 


u = [random.randint(0,9) for y in range(10)]        # вариант 8, №1
print(u)

print(sum(u))

p = math.prod(u)
print(p)

o = [random.randint(0,9) for y in range(10)]        # вариант 8, №2
print(o)

srznach = sum(o)/len(o)
print(srznach)

for a in range(len(o)):
    if o[a] == 0:
        o[a] = srznach

print(o)


n = int(input())                                      # вариант 3, №1
l = [random.randint(0,9) for y in range(n)]
print(l)

m = []
for h in range(len(l)):
    if h%2 != 0:
        m.append(l[h])


print(sum(m))

v = [random.randint(0,20) for y in range(8)]           # вариант 3, №2

for s in range(len(v)):
    if v[s] < 15:
        v[s] = v[s]*2

print(v) 