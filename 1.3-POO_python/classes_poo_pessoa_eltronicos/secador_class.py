from eletrodomesticos_class import Eletrodomestico

class Secador(Eletrodomestico):
    pass
    def __str__(self):
        return f"O secador {self.cor} - custa {self.preco} reais."
    
secador_azul = Secador("azul", 1200, 127, 230)
print(secador_azul)