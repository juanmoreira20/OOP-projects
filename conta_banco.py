#programa desenvolvido para o treino de conceitos básicos da orientação a objeto como encapsulamento, propriedades, métodos estáticos e privados
class Conta:
    def __init__(self, numero, titular, saldo, limite,):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if valor <= self.__saldo + self.limite:
            self.__saldo -= valor
        else:
            print("Não há limite suficiente para o saque")


    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return (self.__limite)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "007"
