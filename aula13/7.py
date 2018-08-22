f = int(input('Quantidade de números das duas sequências:'))
soma = []

print('Insira os números da PRIMEIRA sequência')

seq1 = []

for x in range (1,f+1):
    n = int(input('Número:'))
    seq1.append (n)


print('Insira os números da SEGUNDA sequência')

seq2 = []

for x in range (1,f+1):
    n = int(input('Número:'))
    seq2.append (n)

print ('Sequência 1:', seq1)
print ('Sequência 2:', seq2)

for x in range (0,f):
    soma.append ((seq1[x])+(seq2[x]))

print ('Soma das sequências:', soma)



