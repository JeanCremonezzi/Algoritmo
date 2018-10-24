L1=[]

q= int(input("Informe a quantidade de elementos: "))
f= int(input("Informe o número de potencia: "))
for i in range(0, q):
    n= float(input("Informe um número da L1: "))
    L1.append(n)
def lista():
    L2=[]
    for i in range (0, len(L1)):
        soma= L1[i] ** f
        L2.append(soma)
    return L2


x= lista()
print(x)
