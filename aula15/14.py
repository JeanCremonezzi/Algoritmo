def calc(a, b, c):
    pag = (a * b)+ c
    print(f"A corrida custou R${pag}")


dist = int(input("Distância percorrida (Km): "))
custo = float(input("Custo por Km (R$): "))
band = float(input("Valor da bandeirada (R$): "))

calc(dist,custo,band)
