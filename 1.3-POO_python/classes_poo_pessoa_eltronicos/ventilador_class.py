class Ventilador:
    @property
    def cor(self):
        return self.__cor.upper()
    
    @cor.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "ivisível":
            raise ValueError("Não existe ventilador invisível")
        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0


    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(f"A velocidade deve estar entre 0 e {self.__velocidade_maxima}")

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade
        ) * velocidade
        self.__ligado = True  

    def desligado(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado
    

ventilador_brown = Ventilador("brown", 1200, 127, 230)