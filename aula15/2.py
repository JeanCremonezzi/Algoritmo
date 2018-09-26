def func():
    nome = input('Nome: ')
    idade = int(input("Idade: "))

    if idade >= 18:
        print(nome, 'é maior de idade')
    else:
        print(nome, 'é menor de idade')

func()
