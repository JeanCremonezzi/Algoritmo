n = int(input('Quantidade de notas: '))
ln = []
soma = 0

for x in range (1, n+1):
    ni = int(input('Nota: '))
    ln.append (ni)
    soma = soma + ni
    media = soma / len(ln)

print ('Todas as notas: ', ln)
print ('Média de notas:', media)

