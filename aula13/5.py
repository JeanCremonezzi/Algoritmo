f = int(input('Quantidade de números:'))

seq = []
soma = 0
mult = 1

for x in range (1,f+1):
    n = int(input('Número:'))
    seq.append (n)

    if (n % 2 == 0):
        soma = soma + n

    else:
        mult = mult * n

print ('Sequência original:', seq)
print ('Soma dos pares:', soma)
print ('Multiplicação ímpares:', mult)
