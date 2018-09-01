palavra = input("Palavra: ")
letra = input("Letra: ")

a = ""

for x in palavra:
    if x not in letra:
        a = a + x

print (a)
