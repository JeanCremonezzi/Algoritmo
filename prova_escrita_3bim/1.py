qnt = int(input("Quantidade de elementos: "))
li = []
aux = 0

for x in range (0,qnt):
    el = int(input("Número: "))
    if el > aux:
        li.append(el)

minimo = int(input("Mínimo: "))
maximo = int(input("Máximo"))
nova_lista = []

for y in li:
    if (y >= minimo) and (y <= maximo):
        nova_lista.append(y)

print (nova_lista)
    
    
    
