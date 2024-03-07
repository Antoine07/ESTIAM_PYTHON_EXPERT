# depuis le module Product (Product.py <=> module perso Python) importe la classe Product
from Product import Product 

# tva attribut attaché à la classe 
Product.tva = .10

products = [
    { "name" : "apple", "price" : 0.75},
    { "name" : "orange", "price" : 0.85},
    { "name" : "banana", "price" : 0.90},
    { "name" : "rasberry", "price" : 0.55},
]

# création d'objets à la voler
storage = []

for p in products:
    storage.append(Product(**p))


for p in storage:
    print( p.priceTTC() )