def verif(a):
    x = 0
    if a > 0 :
        x = 1
    elif a < 0:
        x = -1
    else:
        x = 0
    return x

num = int(input("Número: "))

f = verif(num)
print(f)
