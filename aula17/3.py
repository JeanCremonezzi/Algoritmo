from random import randint

def random_elem (num):
    lista = []
    while len(lista) != num:
        aux = randint (-100,100)
        if aux not in lista:
            lista.append(aux)
    return lista
    
def creat_list (l1,l2):
    lista = []

    return lista

num = int(input("Quantidade de elementos das listas: "))

l1= random_elem(num)
l2= random_elem(num)

print (l1)
print (l2)

func_return = creat_list (l1,l2)
print (f"Soma das Listas: {func_return}")
