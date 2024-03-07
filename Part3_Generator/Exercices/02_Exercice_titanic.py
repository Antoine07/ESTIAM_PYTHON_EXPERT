import typing 
import csv 

# définir les classes
class Counter:
    # Un constructeur c'est une méthode qui est appelée lorsqu'on crée un objet
    def __init__(self, count = 0) -> None:
        # définir un attribut 
        self.count =  count 

# structure les données que je vais exploiter dans mon script 
class Passenger:
    def __init__(self, id, survived, name, sex, age ) -> None:
        self.id = id
        self.survived = survived
        self.name = name
        self.sex = sex
        self.age = age

# Création d'une instance de la classe Counter, vous pouvez passer une valeur à votre classe, elle sera récupérée par le constructeur __init__
c = Counter(count = 0)

# pour accéder à un attribut de la classe 
print(c.count)

# création de la fonction générateur
def getBySexAndAge(fileName, age, sex):
    # lecture du fichier 
    with open(fileName, 'r') as f:
        spamreader = csv.reader(f, delimiter=',')  
        for row in spamreader:
            if row[1] == '1' and row[4] == sex and  row[5] != '' and float( row[5] ) >= age:
                p = {'id' : row[0], 'name' : row[3], 'survived' :  row[1], 'sex' : row[4], 'age' :row[5] }

                yield Passenger(**p)

# Créer le générateur
# gen = getBySexAndAge('./Data/titanic.csv', age = 41, sex='female')

# for r in gen:
#     print(r)

# une fois le générateur consommé il faut le recréer
gen = getBySexAndAge('./Data/titanic.csv', age = 41, sex='female')

# Une classe Passenger


try:
    r = next(gen)
    print(r)
    while True:
         passenger= next(gen)
         print(f"{passenger.name}, age : {passenger.age}") 
         # on a une fonction magique sur les objets pour afficher ses attributs 
         print(passenger.__dict__)

except StopIteration as e:
    print(e)