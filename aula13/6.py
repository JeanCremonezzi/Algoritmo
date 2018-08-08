f = int(input('Quantidade de números:'))

seq = []
inv = []

for x in range (1,f+1):
    n = int(input('Número:'))
    seq.append (n)
    inv.insert (0,n)

print('Números na sequência:', seq)
print('Números invertidos:', inv)
