from eletrodomesticos_class import Eletrodomestico

class Liquidificador(Eletrodomestico):
   pass

liquidificador_vermelho = Liquidificador("Vermelho", 250, 220, 100)
liquidificador_vermelho.ligar(1)
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? True
liquidificador_vermelho.desligar()
print("Está ligado?", liquidificador_vermelho.esta_ligado())
# Está ligado? False


liquidificador = Liquidificador("Rosa", "110", "127", "200")

print(liquidificador.cor) # ROSA
liquidificador.cor = "Vermelho"
print(liquidificador.cor) # VERMELHO