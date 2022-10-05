import random
import math
from re import U            
# n = [random.randint(0,9) for i in range(7)]         # варинат 1, №1
# print(n)

# a = max(n)
# print(a)

# n.reverse()

# print(n)

# c = [random.randint(0,9) for y in range(10)]        # варинат 1, №2
# print(c)

# srznach = sum(c)/len(c)
# print(srznach)

# for q in range(len(c)):
#     if c[q] == 0 :
#         c[q] = srznach
# print(c) 


u = [random.randint(0,9) for y in range(10)]        # вариант 8, №1
print(u)
print(sum(u))
p = math.prod(u)
print(p)

o = [random.randint(0,9) for y in range(10)]
