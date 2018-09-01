palavra = input("Palavra: ")
inv = palavra[::-1]

if (palavra == inv):
    print(palavra, 'é palindromo')
else:
    print(palavra, 'NÃO é palindromo')
