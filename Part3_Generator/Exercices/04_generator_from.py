"""
Dans cet exemple, nous utilisons yield from zip(*generator) pour déléguer la génération à zip, qui combine les valeurs produites par chaque générateur en couples. 
Cela permet de générer directement les couples sans avoir à itérer sur chaque générateur individuellement.
"""

def vect(*generator):
    yield from zip( *generator )

# Séquence de nombre entier 
def genRange(start, step, end):
    while start <= end:
        yield start
        start += step

# Affiche les couples de valeurs 1 4 // 2 5 // 3 6
for p, q in vect(genRange(start = 1, step = 1, end = 3),genRange(start = 4, step = 1, end = 6) ):
    print(p, q)
