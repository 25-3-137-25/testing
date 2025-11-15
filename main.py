def puzirek(massiv):
    f = True
    while f:
        f = False
        for i in range(len(massiv)-1):
            if massiv[i] > massiv[i+1]:
                massiv[i], massiv[i+1] = massiv[i+1], massiv[i]
                f = True
    return massiv

def viborka(massiv):
    for i in range(len(massiv)):
        low = i
        for j in range(i + 1, len(massiv)):
            if massiv[j] < massiv[low]:
                low = j
        massiv[i], massiv[low] = massiv[low], massiv[i]
    return massiv

def vstavka(massiv):
    for i in range(1, len(massiv)):
        smth = massiv[i]
        j = i - 1
        while j >= 0 and massiv[j] > smth:
            massiv[j + 1] = massiv[j]
            j -= 1
        massiv[j + 1] = smth
    return massiv

def to2(x):
    k = ""
    while x > 0:
        k += str(x%2)
        x = x//2
    return (k[::-1])

def to8(x):
    k = ""
    while x > 0:
        k += str(x%8)
        x = x//8
    return k[::-1]

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def gosdolg(x):
    if x < 37860000000000:
        return "госдолг сша больше, чем ваше кол-во долларов"
    else:
        return "госдолг сша меньше вашего кол-ва долларов"

def prostoe(x):
    k=0
    for i in range(2,x):
        if x%i==0:
            k+=1
    if k==0:
        return True
    else:
        return False