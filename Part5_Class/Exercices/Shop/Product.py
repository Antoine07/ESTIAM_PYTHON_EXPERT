

class Product:

    tva = .5 # 0.5 <=> .5
    precision = 2

    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value) -> None:
        if type(value) is not str :
            raise ValueError("Attention ce n'est une chaîne de caractères")
        
        self._name = value

    @name.getter
    def name(self):
        return self._name
    
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        if type(value) is not float :
            raise ValueError("Attention ce n'est un numérique")
        
        self._price = value

    @price.getter
    def price(self):
        return self._price
    
    def priceTTC(self):

        return round( self.price * ( 1 + self.tva ),  self.precision )