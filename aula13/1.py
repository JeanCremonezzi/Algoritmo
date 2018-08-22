l = [303,8,0,97,105,21]
maior = 0
soma = 0
imp = []
m18 = []

for x in l:
    if (x > maior):
        maior = x
        menor = maior
    soma = soma + x

    if (x % 2 != 0):
        imp.append (x)

    if (x > 18):
        m18.append (x)

for x in l:
    if (x < menor):
        menor = x

print ('MAIOR :', maior)
print ('MENOR :', menor)
print ('SOMA :', soma)
print ('ÍMPARES :', imp)
print ('MAIORES QUE 18 :', m18)

    
