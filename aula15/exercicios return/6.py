def calc (a,b,c,d):
    media = (a + b + c + d) / 4
    return media
    

num1 = float(input("Nota um: "))
num2 = float(input("Nota dois: "))
num3 = float(input("Nota três: "))
num4 = float(input("Nota quatro: "))

f = calc(num1,num2,num3,num4)
print (round(f,2))
