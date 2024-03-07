class Hello:
    """
        message est attaché à la classe avant tout
        on peut y accéder depuis la classe
    """
    message = "Hello World" # statique attaché à la classe quelque soit l'instance de la classe

    # méthode appelée lorsqu'on crée un objet <=> une instance de classe
    def __init__(self) -> None:
        print(f"Je suis la classe Hello et on vient de créer un objet")

    def getMessage(self):
        return self.message
    

# message est attribut attaché à la classe comme variable statique
print(Hello.message)
h = Hello()

# attaché à l'objet également 
print(h.getMessage())

Hello.message = "Bonjour tout le monde"

i = Hello()
print(i.getMessage())
j = Hello()
print(j.getMessage())

# Avec self <=> est un objet une instance une nouvelle variable 

