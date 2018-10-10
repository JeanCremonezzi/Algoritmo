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
    for x in range(0,len(l1)):
        soma = l1[x] - l2[x]  
        lista.append(soma)
    return lista

num = int(input("Quantidade de elementos das listas: "))

l1= random_elem(num)
l2= random_elem(num)

print (f"Lista 1: {l1}")
print (f"Lista 2: {l2}")

func_return = creat_list (l1,l2)
print (f"Soma das Listas: {func_return}")
