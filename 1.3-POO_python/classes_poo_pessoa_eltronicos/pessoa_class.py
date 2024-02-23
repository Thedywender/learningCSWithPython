from liquidificador_class import liquidificador_vermelho
from ventilador_class import ventilador_brown

class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador


    def __str__(self):
        return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."


    

pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)

pessoa_cozinheira1 = Pessoa("Maria", 2000)
pessoa_cozinheira1.comprar_ventilador(ventilador_brown)

print(pessoa_cozinheira, pessoa_cozinheira1)