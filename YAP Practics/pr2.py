import math # пример № 8

x = float(input())
y = float(input())
z = float(input())

e = math.e
c = x - y
c1 = x + y

a = math.pow(e, abs(c)) * math.pow(abs(c), c1)

b = math.atan(x) + math.atan(z)

u = x**6 + math.log(e, y)**2

t = math.pow(u, 1/3)

w = (a / b) + t
print(w) 