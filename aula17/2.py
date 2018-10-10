import random

def creat_list (num):
    lista = []
    while len(lista) != num:
        aux = random.uniform(-100, 100)
        if aux not in lista:
            lista.append(aux)
    return lista

num = int(input("Quantidade de elementos da Lista: "))
func_return = creat_list (num)

print (f"Lista: {func_return}")

