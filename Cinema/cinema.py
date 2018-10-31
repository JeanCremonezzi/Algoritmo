def IncluirSala (codigo, nome, cap, tipo, acesso):
    sala = {'Código':codigo, 'Nome':nome, 'Capacidade':cap, 'Tipo':tipo, 'Acesso':acesso}
    salas[codigo] = sala
    print ('\n SALA INCLUIDA !!! \n')

def AlterarSala (codigo):
    for x in salas:
        if codigo == x:

            

print ('Menu de Opções: \n 1.Submenu de Salas \n 2.Submenu de Filmes \n 3.Submenu de Sessões \n 4.Sair \n')
opcao = int(input('Valor da Opção: '))

salas = {}
filmes = []
sessoes = []

while opcao >= 1 and opcao < 4: # Loop Menu Principal

    if opcao == 1:  # MENU SALA
        print ('\n SUBMENU DE SALAS: \n 1.Incluir \n 2.Alterar \n 3.Imprimir \n 4.Excluir \n 5.Exibir Sala Específica \n 6.Voltar \n ')
        acao = int(input('Valor Ação Salas: '))
        
        while acao >= 1 and acao <= 5: #Loop Submenu Sala
            if acao == 1: # Incluir
                codigoSala = int(input('Código da Sala: '))
                nomeSala = input('Nome da Sala: ')
                capacidadeSala = int(input('Capacidade da Sala: '))
                tipoSala = input('Tipo de Sala: ')
                acessoSala = input('Acesso da Sala (True/False): ')
                IncluirSala(codigoSala,nomeSala,capacidadeSala,tipoSala,acessoSala)
               
            if acao == 2: # Alterar
                altSala = int(input('Código da Sala para Alterar: '))
                AlterarSala(altSala)
                
            if acao == 3: # Imprimir
                print ('salas.3')
                
            if acao == 4: # Excluir
                print ('salas.4')
                
            if acao == 5: # Exibir Sala
                print ('salas.5')
                
            if acao == 6: # Voltar
                exit
                
            acao = int(input('Valor Ação Salas: '))
                     
    if opcao == 2: # MENU FILMES
        print ('2')
        
    if opcao == 3: # MENU SESSÃO
        print ('3')
        
    if opcao == 4: # SAIR
        exit

    opcao = int(input('Valor da Opção: '))
