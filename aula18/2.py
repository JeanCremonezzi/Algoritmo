def menu():
    dic_tel = {}
    opção = 0
    while opção < 5:
        print("Menu Principal:")
        print("1. Inserir Nome e Telefone")
        print("2. Incluir Telefone")
        print("3. Excluir Telefone")
        print("4. Excluir Nome")
        print("5. Sair")
        print("------------------------------------------")
        opção = int(input("Digite a opção: "))
        print("------------------------------------------")
        if opção == 1:
            InsereNome(dic_tel)
        elif opção == 2:
            InsereTel(dic_tel)
        elif opção == 3:
            DeletaTel(dic_tel)
        elif opção == 4:
            DeletaNome(dic_tel)
        else:
            print("Programa Encerrado!")


def InsereNome(dic_tel):
    teles = []
    aux = 0
    nome = input("Nome: ")
    while nome in dic_tel:
        nome = input("Esse nome já está na lista, digite outro nome: ")
            
    qnt = int(input("Quantos números você vai digitar?  "))
    while aux < qnt:
        tel = int(input("Digite o telefone: "))
        teles.append(tel)
        aux = aux + 1
    dic_tel[nome] = teles
    print(dic_tel)
    print("------------------------------------------")

def InsereTel(dic_tel):
    print(dic_tel)
    inc = input("Em qual nome você deseja incluir o telefone? ")
    while inc not in dic_tel:
        inc = input("Esse nome não está na lista, digite corretamente o nome: ")
            
    for chaves in dic_tel.keys():
        if chaves == inc:
            telo = int(input("Digite o telefone: "))
            dic_tel[chaves].append(telo)
            
    print(dic_tel)
    print("------------------------------------------")

def DeletaTel(dic_tel):
    print(dic_tel)
    inc2 = input("De qual nome você deseja excluir um telefone? ")
    while inc2 not in dic_tel:
        inc2 = input("Esse nome não está na lista, digite corretamente o nome: ")
        
    if inc2 in dic_tel.keys():
        lista_num = dic_tel.get(inc2)
        valor = int(input("Digite qual número você quer apagar: "))
        if valor in lista_num:
           i =  lista_num.index(valor)
           del lista_num[i]
        
        else:
            print("Este número não está registrado!")
            valor = int(input("Digite corretamente o número que você quer apagar: "))
            if valor in lista_num:
               i =  lista_num.index(valor)
               del lista_num[i]
        print(dic_tel)
        print("------------------------------------------")
    

def DeletaNome(dic_tel):
    print(dic_tel)
    inc3 = input("Qual nome você deseja excluir? ")
    while inc3 not in dic_tel:
        inc3 = input("Esse nome não está na lista, digite corretamente o nome: ")
        
    if inc3 in dic_tel.keys():
        del dic_tel[inc3]
        
    print(dic_tel)
    print("------------------------------------------")


#Principal
menu()
