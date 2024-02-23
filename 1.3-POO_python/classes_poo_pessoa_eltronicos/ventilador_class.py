from eletrodomesticos_class import Eletrodomestico

class Ventilador(Eletrodomestico):
    pass
    def __str__(self):
        return f"O ventilador {self.cor} - custa {self.preco} reais."


ventilador_preto = Ventilador("preto", 1200, 127, 230)  

ventilador_brown = Ventilador("brown", 1200, 127, 230)

print(ventilador_brown)
print(ventilador_preto)