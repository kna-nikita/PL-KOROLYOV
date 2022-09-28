a =int(input())         # пример №1
b = int(input())

if a <= b:
    for i in range(a, b+1):
        print(i) 
else:
    print("введите числа заново, а должно быть <= b")



n = int(input('введите количество слагаемых:'))   # пример №4
c = 0
print("введите эти слагаемые")
for i in range(n):
    m = int(input())
    c = c + m
print(c)


n = int(input()     # пример №5
c = 1
m = 0

for i in range(n):
    e = c ** 3
    c += 1
    m += e
print(m) 