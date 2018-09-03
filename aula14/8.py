frase = input("Frase: ")
vogais = "aeiouAEIOU"
total_vogais= 0
espaco = 0

for x in frase:
    if x in vogais:
        total_vogais = total_vogais + 1

    if x == " ":
        espaco = espaco +1
    
print ('Quantidade de Espaços:',espaco)
print ('Quantidade total de Vogais:',total_vogais)
        
    
