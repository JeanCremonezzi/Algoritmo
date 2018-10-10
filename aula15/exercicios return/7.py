def calc (a,b,c,d):
    media = (a + b + c + d) / 4
    apr = ""
    if media >=6:
        apr = True
    else:
        apr = False
    return apr
    

num1 = float(input("Nota um: "))
num2 = float(input("Nota dois: "))
num3 = float(input("Nota três: "))
num4 = float(input("Nota quatro: "))

f = calc(num1,num2,num3,num4)
if f:
    print('Verdadeiro')
else:
    print('Falso')

