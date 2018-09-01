frase = input("Frase: ")
vogais = "aeiouAEIOU"
total_vogais= 0
a = 0
e = 0
i = 0
o = 0
u = 0
espaco = 0

for x in frase:
    if x in vogais:
        total_vogais = total_vogais + 1

    if x == "a" or x == "A":
        a = a +1

    if x == "e" or x == "E":
        e = e +1

    if x == "i" or x == "I":
        i = i +1

    if x == "o" or x == "O":
        o = o +1
        
    if x == "u" or x == "U":
        u = u +1

    if x == " ":
        espaco = espaco +1
    
print ('Quantidade de Espaços:',espaco)
print ('Quantidade de "A/a":',a)
print ('Quantidade de "E/e":',e)
print ('Quantidade de "I/i":',i)
print ('Quantidade de "O/o":',o)
print ('Quantidade de "U/u":',u)
print ('Quantidade total de Vogais:',total_vogais)
        
    
