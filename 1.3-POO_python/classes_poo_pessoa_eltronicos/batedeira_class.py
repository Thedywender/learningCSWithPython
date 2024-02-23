from eletrodomesticos_class import Eletrodomestico

class Batedeira(Eletrodomestico):
    pass
    def __str__(self):
        return f"A batedeira {self.cor} - custa {self.preco} reais."
    

batedeira_branca = Batedeira("branca", 1200, 127, 230)
print(batedeira_branca)