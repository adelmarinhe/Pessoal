from Conta import Conta

class ContaPoupanca(Conta):
    __rendimento = 0

    def __init__(self, numConta: int, numAg: int, banco: int, nome: str, cpf: int, rendimento: float, saldo: float = 0) -> None:
        super().__init__(numConta, numAg, banco, nome, cpf, saldo)
        if rendimento < 0:
            raise ValueError("O rendimento da conta não pode ser negativo.")
        self.__rendimento = rendimento

    def renderJuros(self):
        print(f"Sua conta rendeu um valor de R${self.getSaldo()*self.__rendimento}")
        self.receber(self.getSaldo()*self.__rendimento)
        print(f"Seu novo saldo é R${self.getSaldo()}")

if __name__ == "__main__":
    '''conta1 = ContaPoupanca(123, 123, 123, "rafael", 123, 0.01, 100)

    conta1.renderJuros()

    print(conta1.getSaldo())'''