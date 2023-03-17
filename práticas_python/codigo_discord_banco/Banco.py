from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class Banco():
    __nome = ""
    __contas = {}
    __numAg = 0
    __numBanco = 0

    def __init__(self, nome: str, numeroAg: int, numeroBanco: int) -> None:
        self.__nome = nome
        self.__numAg = numeroAg
        self.__numBanco = numeroBanco

    def criarContaCorrente(self, numeroConta: int, nome: str, cpf: int, credito: float, saldo: float) -> None:
        if numeroConta in self.__contas:
            print("Já existe uma conta com este número de identificação.")
        else:
            try:
                self.__contas[numeroConta] = ContaCorrente(numeroConta, self.__numAg, self.__numBanco, nome, cpf, credito, saldo)
            except Exception as erro:
                print(erro)

    def criarContaPoupanca(self, numeroConta: int, nome: str, cpf: int, rendimento: float, saldo: float) -> None:
        if numeroConta in self.__contas:
            print("Já existe uma conta com este número de identificação.")
        else:
            try:
                self.__contas[numeroConta] = ContaPoupanca(numeroConta, self.__numAg, self.__numBanco, nome, cpf, rendimento, saldo)
            except Exception as erro:
                print(erro)

    def sacar(self, numeroConta: int, valor: float) -> None:
        if numeroConta not in self.__contas:
            print("Essa conta não existe.")
        else:
            try:
                self.__contas[numeroConta].sacar(valor)
            except Exception as erro:
                print(erro)

    def depositar(self, numeroConta: int, valor: float) -> None:
        if numeroConta not in self.__contas:
            print("Essa conta não existe.")
        else:
            try:
                self.__contas[numeroConta].depositar(valor)
            except Exception as erro:
                print(erro)

    def transferir(self, numeroContaSai: int, numeroContaEntra: int, valor: float) -> None:
        if numeroContaSai not in self.__contas or numeroContaEntra not in self.__contas:
            print("Ambas as contas devem ser existentes.")
        else:
            try:
                self.__contas[numeroContaSai].transferir(valor, self.__contas[numeroContaEntra])
            except Exception as erro:
                print(erro)

    def compraCredito(self, numeroConta: int, valor: float) -> None:
        if numeroConta not in self.__contas:
            print("Essa conta não existe.")
        elif type(self.__contas[numeroConta]) != ContaCorrente:
            print("A conta deve ser do tipo conta corrente para realizar compra no crédito.")
        else:
            try:
                self.__contas[numeroConta].compraCredito(valor)
            except Exception as erro:
                print(erro)

    def pagarFatura(self, numeroConta: int, valor: float) -> None:
        if numeroConta not in self.__contas:
            print("Essa conta não existe.")
        elif type(self.__contas[numeroConta]) != ContaCorrente:
            print("A conta deve ser do tipo conta corrente para realizar pagamento de fatura.")
        else:
            try:
                self.__contas[numeroConta].pagarFatura(valor)
            except Exception as erro:
                print(erro)

    def renderJuros(self, numeroConta: int) -> None:
        if numeroConta not in self.__contas:
            print("Essa conta não existe.")
        elif type(self.__contas[numeroConta]) != ContaPoupanca:
            print("O rendimento de juros é uma função disponível apenas para contas do tipo poupança.")
        else:
            self.__contas[numeroConta].renderJuros()

    def renderTodasContas(self) -> None:
        for conta in self.__contas:
            if type(self.__contas[conta]) == ContaPoupanca:
                self.__contas[conta].renderJuros()

    def statusTodasContas(self) -> None:
        for conta in self.__contas:
            print(f"Conta: {conta}\tSaldo: R${self.__contas[conta].getSaldo()}", end = "")
            if type(self.__contas[conta]) == ContaCorrente:
                print(f"\tCredito Disponível: {self.__contas[conta].getCreditoDisponivel()}", end = "")
            print()

if __name__ == "__main__":
    banco = Banco("Banco CIn", 123, 123)
    banco.criarContaCorrente(222, "Rafael", 123, 15, 5000)
    banco.criarContaPoupanca(333, "José", 234, 0.01, 2000)
    banco.criarContaPoupanca(444, "Tiago", 234, 0.01, 1000)
    
    '''banco.sacar(222, 100)
    banco.sacar(333, 10)
    banco.transferir(222, 333, 250)'''

    banco.compraCredito(222, 20)
    banco.compraCredito(222, 10)
    banco.pagarFatura(222, 10)

    banco.compraCredito(333, 700)
    banco.renderTodasContas()

    banco.statusTodasContas()