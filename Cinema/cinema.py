def incluirSala(codigo, nome, cap, tipo, acesso): # FUNÇÃO PARA INCLUIR SALAS
    sala = {'codigo':codigo, 'nome':nome, 'capacidade':cap, 'tipo':tipo, 'acesso':acesso}
    if codigo in salas:
        print('\n Sala já existente !')
    else:
        salas[codigo] = sala
        print ('\n --SALA INCLUÍDA-- \n')

def alterarSala(codigo): # FUNÇÃO PARA ALTERAR SALAS
    if codigo in salas:
        del salas[codigo]
        codigoSala = int(input('Codigo da Sala: '))
        nomeSala = input('Nome da Sala: ')
        capSala = int(input('Capacidade da Sala: '))
        tipoSala = input('Tipo de Sala: ')
        acessoSala = input('Acesso da Sala (True/False): ')
        sala = {'codigo':codigoSala, 'nome':nomeSala, 'capacidade':capSala, 'tipo':tipoSala, 'acesso':acessoSala}
        salas[codigoSala] = sala
        print ('\n --SALA ALTERADA-- \n')
    else:
        print('Sala não Existente')
        
def excluirSala(codigo): # FUNÇÃO PARA EXCLUIR SALAS
    if codigo in salas:
        del salas[codigo]
        print ('Sala ',codigo,' excluída')
    else:
        print('Sala não Existente !')

def exibirSala(codigo): # FUNÇÃO PARA EXIBIR SALAS ESPECÍFICAS
    if codigo in salas:
        print(salas[codigo])
    else:
        print('Sala não Existente !')

def atores(): # FUNÇÃO PARA DETERMINAR ATORES
    ator = input('Ator (Digite "fim" para terminar): ')
    while ator != 'fim':
        atoresFilme.append(ator)
        ator = input('Ator (Digite "fim" para terminar): ')

def incluirFilme(codigo, nome, ano, diretor, atores): # FUNÇÃO PARA EXIBIR FILMES
    filme = {'codigo':codigo, 'nome':nome, 'lançamento':ano, 'diretor':diretor, 'atores':atores}
    if codigo in filmes:
        print('\n Filme já existente !')
    else:
        filmes[codigo] = filme
        print ('\n --FILME INCLUÍDO-- \n')

def alterarFilme(codigo): # FUNÇÃO PARA ALTERAR FILME
    if codigo in filmes:
        del filmes[codigo]
        codigoFilme = int(input('Codigo do Filme: '))
        nomeFilme = input('Nome do Filme: ')
        anoFilme = int(input('Ano de Lançamento do Filme: '))
        diretorFilme = input('Diretor do Filme: ')
        atoresFilme = []
        atores()
        filme = {'codigo':codigoFilme, 'nome':nomeFilme, 'lançamento':anoFilme, 'diretor':diretorFilme, 'atores':atoresFilme}
        filmes[codigoFilme] = filme
        print ('\n --FILME ALTERADO-- \n')
    else:
        print('Sala não Existente')

def excluirFilme(codigo): # FUNÇÃO PARA EXCLUIR FILME
    if codigo in filmes:
        del filmes[codigo]
        print ('Filme ',codigo,' excluído')
    else:
        print('Filme não Existente !')

def exibirFilme(codigo): # FUNÇÃO PARA EXIBIR FILME ESPECÍFICO
    if codigo in filmes:
        print(filmes[codigo])
    else:
        print('Sala não Existente !')
        
def incluirSessao():
   
salas = {} # DICT DE SALAS
filmes = {} # DICT DE FILMES
sessoes = {} # DICT DE SESSÕES
        
print ('---MENU PRINCIPAL--- \n 1.SALAS \n 2.FILMES \n 3.SESSÕES \n 4.SAIR')
opcao = int(input('\n ESCOLHA UMA OPÇÃO:'))
xxx = 0

while xxx == 0:
    if opcao == 1:
        print ('\n ---SUBMENU DE SALAS--- \n 1.Incluir \n 2.Alterar \n 3.Imprimir \n 4.Excluir \n 5.Exibir Sala Específica')
        opcaoSala = int(input('\n AÇÃO SALAS: '))

        if opcaoSala == 1 : # ESCOLHEU INCLUIR SALA
            codigoSala = int(input('Codigo da Sala: '))
            nomeSala = input('Nome da Sala: ')
            capSala = int(input('Capacidade da Sala: '))
            tipoSala = input('Tipo de Sala: ')
            acessoSala = input('Acesso da Sala (True/False): ')
            incluirSala(codigoSala, nomeSala, capSala, tipoSala, acessoSala)
                
        elif opcaoSala == 2: # ESCOLHEU ALTERAR SALA
            codigoSala = int(input('Informe o CÓDIGO da SALA: '))
            alterarSala(codigoSala)
                
        elif opcaoSala == 3: # ESCOLHEU EXIBIR TODAS SALAS
            print(salas) # IMPRIME DICT SALAS
                
        elif opcaoSala == 4: # ESCOLHEU EXCLUIR SALA
            codigoSala = int(input('Código da Sala para excluir: '))
            excluirSala(codigoSala)
                
        elif opcaoSala == 5: # ESCOLHEU EXIBIR SALA ESPECÍFICA
            codigoSala = int(input('Código da Sala para exibir: '))
            exibirSala(codigoSala)
        
    elif opcao == 2:
        print ('\n SUBMENU DE FILMES: \n 1.Incluir \n 2.Alterar \n 3.Imprimir \n 4.Excluir \n 5.Exibir Filme Específico')
        opcaoFilme = int(input('Ação Filmes: '))
        
        if opcaoFilme == 1: # ESCOLHEU INCLUIR FILME
            codigoFilme = int(input('Codigo do Filme: '))
            nomeFilme = input('Nome do Filme: ')
            anoFilme = int(input('Ano de Lançamento do Filme: '))
            diretorFilme = input('Diretor do Filme: ')
            atoresFilme = []
            atores()
            incluirFilme(codigoFilme, nomeFilme, anoFilme, diretorFilme, atoresFilme)

        if opcaoFilme == 2: # ESCOLHEU ALTERAR FILME
            codigoFilme = int(input('Informe o CÓDIGO do FILME: '))
            alterarFilme(codigoFilme)
                
        if opcaoFilme == 3: # ESCOLHEU EXIBIR FILMES
            print(filmes)

        if opcaoFilme == 4: # ESCOLHEU EXCLUIR FILME
            codigoFilme = int(input('Código do Filme para excluir: '))
            excluirFilme(codigoFilme)

        if opcaoFilme == 5: # ESCOLHEU EXIBIR FILME ESPECIFICO
            codigoFilme = int(input('Código do Filme para exibir: '))
            exibirFilme(codigoFilme)
                
    elif opcao == 3:
        print ('\n SUBMENU DE SESSÕES: \n 1.Incluir \n 2.Alterar \n 3.Imprimir \n 4.Excluir \n 5.Exibir Sessão Específica')
        opcaoSessao = int(input('Ação Sessões: '))
        
    elif opcao == 4:
        print('\n EXECUÇÃO ENCERRADA \n')
        exit()
    else:
        print('\n --ESCOLHA UMA OPÇÃO VÁLIDA-- \n')

    print ('---MENU PRINCIPAL--- \n 1.SALAS \n 2.FILMES \n 3.SESSÕES \n 4.SAIR')
    opcao = int(input('\n ESCOLHA UMA OPÇÃO:'))
