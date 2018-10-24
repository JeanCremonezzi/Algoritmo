L1=[]
L2=[]
q= int(input("Informe a quantidade de elementos: "))
for i in range(0, q):
    n= int(input("Informe um número da L1: "))
    L1.append(n)
for i in range(0, q):
    n= int(input("Informe um número da L2: "))
    L2.append(n)
def intersecçao():
    L3=[]
    for x in L1:
        if x in L2:
            if x not in L3:
                L3.append(x)
    return L3
y= intersecçao()
print(y)

