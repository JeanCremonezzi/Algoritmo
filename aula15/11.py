def verifica(a,b):
    if a > b:
        print(f"{a} é maior que {b}")
    elif a == b:
        print(f"{a} é igual a {b}")
    else:
        print(f"{b} é maior que {a}")

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

verifica(num1,num2)
