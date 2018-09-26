def calc(a, b, c):
    x = (a * b) + c
    return x

dist = int(input("Distância (Km): "))
val = float(input("Valor por Km (R$): "))
ban = float(input("Bandeirada (R$): "))

preco = calc(dist, val, ban)
print(preco)
