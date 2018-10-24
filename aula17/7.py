L1=[]
L2=[]

q= int(input("Informe a quantidade de elementos: "))
for i in range(0, q):
    n= int(input("Informe um número da L1: "))
    L1.append(n)
for i in range(0, q):
    n= int(input("Informe um número da L2: "))
    L2.append(n)
def lista():
    L3=[]
    soma = 0
    for i in range (len(L1)):
        mult= L1[i] * L2[i]
        L3.append(mult)
        print(L3)
    for i in L3:
        soma = soma + i
    return soma
                  
x= lista()
print(x)
    
