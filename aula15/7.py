def func(a):
    if a < 0:
        print(f"{a} é negativo")
    elif a > 0:
        print(f"{a} é positivo")
    else:
        print(f"{a} é igual a 0")

num = int(input("Número: "))
func(num)
