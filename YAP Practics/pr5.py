a = input()         # пример №15

c = 0

for i in range(len(a)):
    if a[i] == "т":
        c += 1
    else:
        continue

print("количество букв т =", c)  