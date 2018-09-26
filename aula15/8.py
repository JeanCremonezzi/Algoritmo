def mes(a):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    if a in range(1,len(meses)+1):
        print(meses[a-1])
    else:
        print('Mês inválido')

num = int(input("Número do mês: "))
mes(num)
