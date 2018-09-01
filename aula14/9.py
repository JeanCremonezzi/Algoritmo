p1 = input("Palavra Base: ").lower()
p2 = input("Palavra Comparar: ").lower()

a = ""

for x in p1:
    if p1.count(x) == p2.count(x):
        a = a + x

if p1 == "" or p2 == "":
    print ('NÃO é anagrama')

elif len(a) == len(p1):
    print ('É anagrama')

else:
    print ('NÃO é anagrama')


