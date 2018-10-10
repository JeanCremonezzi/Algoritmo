from random import randint

def random_elem (num):
    lista = []
    while len(lista) != num:
        aux = randint (-100,100)
        if aux not in lista:
            lista.append(aux)
    return lista
    
def creat_list (l1,a):
    lista = []
    y = 0
    for x in l1:
        y = x * a
        lista.append(y)
    return lista

num = int(input("Quantidade de elementos das listas: "))
mult = int(input("Multiplicador: "))

l1= random_elem(num,mult)

print (f"Lista 1: {l1}")

func_return = creat_list (l1)
print (f"Multiplicação da Lista: {func_return}")
