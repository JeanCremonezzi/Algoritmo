def func(a, b):
    maior = 0
    if a > b:
        maior = a
    else:
        maior = b
    return maior

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

p = func(num1, num2)
print(p)
