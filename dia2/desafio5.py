class animal:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def som(self):
        return "som do animal"
    
    def apresentar(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos."

class gato(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def som(self):  
        return "Miau!"
    
class cachorro(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def som(self):
        return "Au Au!"
    
cachorro_dados = cachorro("pluto", 3)
gato_dados = gato("bichano", 2)

print(cachorro_dados.som())
print(cachorro_dados.apresentar())

print(gato_dados.som())
print(gato_dados.apresentar())