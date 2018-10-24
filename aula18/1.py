pirata = {'sir':'matey ', 'hotel':'fleabag inn ', 'student':'swabbie ', 'boy':'matey ', 'madam':'proud beauty ', 'professor':'foul blaggart ', 'restaurant':'galley ', 'your':'yer ', 'excuse':'arr ', 'students':'swabbies ', 'are':'be ', 'lawyer':'foul blaggart ', 'the':"th' ", 'restroom':'head ', 'my':'me ', 'hello':'avast ', 'is':'be ', 'man':'matey '}

ing = input('Frase em Inglês: ').split()
pir = ''

for x in ing:
    for y in pirata.keys():
        if x == y:
            pir = pir + pirata[y]

print (pir)
        



