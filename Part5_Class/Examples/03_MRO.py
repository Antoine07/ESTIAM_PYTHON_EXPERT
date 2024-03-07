# Héritage classique une classe hérite d'une autre classe
class Model:
    def __init__(self, name) -> None:
         self.name = name

    def getName(self):
        return self.name

#héritage de la méthode getName
class Post(Model):
    pass 

p = Post(name = "article")
print(p.getName())

# Dans Python de a de l'héritage multiple 
class A:
    def say(self):
        print("Hello A")

class B(A):
    def say(self):
        print("Hello B")

b = B() # la méthode say de B qui est appellée

print("-----------")

b.say()

print("-----------")

class C(A):
    def say(self):
        print("Hello C")

# héritage multiple 
class D(B, C):
    pass

# Création d'une instance de la classe D
print("-----------")
d= D()
d.say()  # MRO (Method Resolution Order) la méthode de la classe B est appelée
print("-----------")

class D(C, B):
    pass

print("-----------")
d= D() # méthode de la classe C qui va être appelée
d.say() 
print("-----------")
