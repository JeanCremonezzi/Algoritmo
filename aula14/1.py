palavra = input("Palavra: ")
letra = input("Letra: ")

a = palavra.index(letra)
b = ""

for x in range (len(palavra)):
    if a != x:
        b = b + palavra[x]

print (b)
