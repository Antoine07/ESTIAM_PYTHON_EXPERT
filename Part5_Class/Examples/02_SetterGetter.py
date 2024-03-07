

class Person:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str :
            raise ValueError("Attention ce n'est une chaîne de caractères")
        
        self._name = value

    @name.getter
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

try:
    person = Person()

    person.name = "Alan"

    print(person.name)
    person.name = 123

except ValueError as e:
    print(e)
finally:
    print("message après le bloc")