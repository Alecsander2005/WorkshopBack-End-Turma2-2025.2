class animal:
    def som(self):
        return "som do animal"
    
class gato(animal):
    def som(self):
        return "Miau!"
    
class cachorro(animal):
    def som(self):
        return "Au Au!"
    
print(cachorro().som())
print(gato().som())