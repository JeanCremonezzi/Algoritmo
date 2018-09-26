def calc(a,b):
    n = (desc/100)*valor
    valor_desc = valor - n
    print(f"Valor com desconto: {valor_desc}")
    
valor = float(input("Valor: "))
desc = int(input("Desconto (%): "))

calc(valor,desc)
