def CalcMedia (NotasAlunos):
    medias = {}
    nomesOrdem = []
    mediasOrdem = []
    for x in NotasAlunos:
        nome = x
        notas = NotasAlunos[x]
        qnt = len(notas)
        soma = 0
        if qnt >= 1:
            for y in notas:
                soma += y
            media = soma/qnt
            medias[nome] = media
        else:
            media = 0
            medias[nome] = media


NotasAlunos = {'João Augusto dos Santos':[8.5,9.2,9.7],
               'Maria Cristina Carvalho':[9.1,8.8],
               'Luiz Augusto de Souza':[],
               'Joana da Silva Prado':[9.5,9.8,9.0,9.9]
               }

CalcMedia(NotasAlunos)

