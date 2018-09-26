def calc(a,b):
    x = a - ((b / 100) * a)
    return x

valor_sd = float(input("Valor (R$): "))
desconto = int(input("Desconto (%): "))

valor_cd = calc(valor_sd, desconto)
print(valor_cd)
