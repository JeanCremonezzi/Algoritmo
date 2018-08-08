l = []
r = []
s= []

f = int(input('Quantidade de números:'))

for x in range (1,f+1):
    n = int(input('Número:'))

    if (n in l):
        p = l.index (n)
        del l[p]
        r.append (n)
        l.append (n)
                             
    else:
        l.append (n)

    s.append (n)

print ('Sequência inserida: ', s)
print ('Número REPETIDOS: ', r)
print ('Números SEM repetição: ', l)





