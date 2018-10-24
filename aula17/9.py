L1=[]
L2=[]
q1= int(input("Informe a quantidade de elementos L1: "))
for i in range(0, q1):
    n= int(input("Informe um número da L1: "))
    L1.append(n)
q2= int(input("Informe a quantidade de elementos L2: "))
for i in range(0, q2):
    n= int(input("Informe um número da L2: "))
    L2.append(n)
def uniao():
    L3=[]
    for x in L1:
        if x not in L3:
            L3.append(x)
    for x in L2:
        if x not in L3:
            L3.append(x)
    return L3
y= uniao()
print(y)
        
