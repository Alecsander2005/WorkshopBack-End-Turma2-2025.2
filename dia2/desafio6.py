class zoologico:
    def __init__(self):
        self.animais = []

    def apresentar(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos."
    
    def adicionar_animais(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [f"{a.apresentar()} faz: {a.som()}" for a in self.animais]
    
    def filtrar_por_tipo(self,tipo):
        return [a for a in self.animais if isinstance(a, tipo)]