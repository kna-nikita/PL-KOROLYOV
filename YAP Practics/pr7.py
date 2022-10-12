import math

def S(a):                                  # вариант2 №1
    
    t = (a**2 * math.sqrt(3)) / 4
    S = t * 6
    return S

print(S(int(input())))        

def Q():                                    # вариант2 №2
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    a3 = int(input())
    b3 = int(input())
    
    S1 = a1 * b1
    S2 = a2 * b2
    S3 = a3 * b3
    
    return S1, S2, S3

print(Q())

def F():                                       # вариант3 №1
    
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())

    g1 = math.sqrt(a1 ** 2 + b1 ** 2)
    g2 = math.sqrt(a2 ** 2 + b2 ** 2)
    
    if g1 > g2:
        print("первая гипотенуза больше, вторая меньше")
    elif g2 > g1:
        print("вторая гипотенуза больше, первая меньше")
    
print(F())

def G():                                        # вариант3 №2
    
    a = '' 
    b = input().lower().split()
    
    for i in range(len(b)):
        b[i] = sorted(b[i])
        a += ''.join(b[i]) + ''
    
    b = a

    return b

print(G())