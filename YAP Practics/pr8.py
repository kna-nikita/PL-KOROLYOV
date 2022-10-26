import random            # вариант1 №1
from random import *

n = (int(input()))  

a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(-9,9)) 
    a.append(b) 

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

print()

x = 0
s = 0
t = 0
for i in range(n):
    x += 1
    for j in range(x,n):
        if a[i][j] > 0:
            s += 1
            t += a[i][j] 

print(s, t) 


             

n = (int(input()))  # кол-во строк               # вариант1 №2
m = (int(input()))  # кол-во столбцов

a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(randint(-9,9)) 
    a.append(b) 

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()

print()


for i in range(n):
    first = a[i][0]
    last = a[i][m - 1]
    min_index = 0
    max_index = 0
    min = 10
    max = -10
    for j in range(m):
        if a[i][j] > max:
            max_index = j
            max = a[i][j]
            print("max_index = ",max_index, max)
        if a[i][j] < min:
            min_index = j 
            min = a[i][j]
            print("min_index = ",min_index, min)
    a[i][0] = max
    a[i][m - 1] = min
    a[i][max_index] = first
    a[i][min_index] = last

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()

print()


n = 3                                  #вариант2 №2

a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(-9,9)) 
    a.append(b) 
for i in range(n):
    for j in range(n):
        print(a[i][j],end = ' ')
    print()
print()


for i in range(n):
    for j in range(n):
        q = a[0][0]
        r = a[1][0]
        t = a[2][0] 

        a[0][0] = a[0][2] 
        a[0][2] = q
        
        a[1][0] = a[1][2]
        a[1][2] = r
        
        a[2][0] = a[2][2]
        a[2][2] = t
        print(a[i][j],end = ' ')
    print()
print()