a = int(input())    # пример №1
b = int(input())

if a < b:
    x = a + b
elif a > b:
    x = a - b
elif a == b:
    x = 1

print(x) 

f = int(input())    # пример №2
k = int(input())

if f < 5 and k > 2:
    R = f + k - 1
elif k < 2:
    R = k**2
elif k == 2:
    R = 1

print(R)

a = int(input())    # пример №3    
b = int(input())

if a < b:
    C = a + b
elif a > b and a > 3:
    C = b**2 - b
else:
    C = b**2 - 1

print(C)

v = int(input())    # пример №4
k = int(input())

if v < k:
    Z = v - k
elif k > v:
    Z = k**2 - v**2
else:
    Z = k**2 - k

print(Z)

f = int(input())    # пример №5

if f < 5:
    z = f + 2
elif f > 5:
    z = f - 1
elif f == 5:
    z = 1

print(z)

a = int(input())    # пример №6
b = int(input())

if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a**2

print(x)

v = int(input())    # пример №7
k = int(input())

if v > 2 and k == 1:
    B = v - k + 1
elif k > v:
    B = k**2 + v**2
else:
    B = k**2 + v

print(B)

x = int(input())     # пример №8
y = int(input())

if x < 2 and y == 2:
    B = x * y + 1
elif x > y:
    B = y**2 + x**2
else:
    B = x**2 + 2

print(B)

f = int(input())    # пример №9
v = int(input())

if f < 4 and v > 6:
    S = f + v
elif v < 6:
    S = k**2
else:
    S = 2 * v

print(S)

k = int(input())    # пример №10
c = int(input())

if k < 5 and c > 4:
    X = k + c**2
elif k > c and k > 3:
    X = c**2 + 2
else:
    X = c - 1

print(X) 