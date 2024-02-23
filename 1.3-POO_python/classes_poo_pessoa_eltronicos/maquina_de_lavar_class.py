from eletrodomesticos_class import Eletrodomestico

class MaquinaDeLavar(Eletrodomestico):
    pass
    def __str__(self):
        return f"A máquina de lavar {self.cor} - custa {self.preco} reais."
    

maquina_de_lavar_branca = MaquinaDeLavar("branca", 1200, 127, 230)
print(maquina_de_lavar_branca)

