def soma_func(y):
    soma = 0
    for z in y:
        soma = soma + z
    return soma
    
lista = []
qnt = int(input("Quantidade de elementos da lista: "))
          
for x in range(0,qnt):
    a = int(input("Elemento da lista: "))
    lista.append(a)

f = soma_func(lista)
print(f'A soma dos elementos da lista é: {f}')
