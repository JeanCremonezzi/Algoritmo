p1 = input("Palavra Base: ").lower()
p2 = input("Palavra Comparar: ").lower()

a = ""

ep1 = ""
ep2 = ""

for y in p1:
    ep1 = (ep1 + y).rstrip()

for y in p2:
    ep2 = (ep2 + y).rstrip()

for x in ep1:
    if ep1.count(x) == ep2.count(x):
        a = a + x

if ep1 == "" or ep2 == "":
    print ('NÃO é anagrama')

elif len(a) == len(ep1):
    print ('É anagrama')

else:
    print ('NÃO é anagrama')
