def func(nome, idade):
    if idade >= 18:
        print(nome, 'é maior de idade')
    else:
        print(nome, 'é menor de idade')

a = input("Nome: ")
b = int(input("Idade: "))
func(a,b)
