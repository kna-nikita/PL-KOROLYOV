def poluchit_ostatok(cifri, delitel, dlina):              #Блок А задание №2
    print(cifri, delitel, dlina)
    delimoe = int(cifri[:dlina])
    
    if delimoe < delitel:
       delimoe = int(cifri[:dlina + 1]) 
     
    ostatok = delimoe % delitel

    if (len(cifri) < dlina) or (len(cifri) == dlina and ostatok < delitel):
        return ostatok
    
    if ostatok !=0:    
        n = str(ostatok) + cifri[len(str(delimoe)):]
    else:
        n = cifri[len(str(delimoe)):] 

    return poluchit_ostatok(n, delitel, dlina)

def poluchit_max():                                       #Блок Б задание №1
    try:
        cifra = int(input())
    except:
        cifra = 0
    
    if cifra == 0:
        return cifra
    return max(poluchit_max(),cifra)


# a = 55555625555
# b = 3

# ostatok = poluchit_ostatok(str(a), b, len(str(b)))

# print('остаток =',ostatok)

max = poluchit_max()
print('max =', max) 