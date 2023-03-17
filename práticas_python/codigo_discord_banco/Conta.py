class Conta():
    __numeroConta = 0
    __numeroAgencia = 0
    __banco = 0
    __nomeTitular = ""
    __cpfTitular = 0
    __saldo = 0

    def __init__(self, numConta: int, numAg: int, banco: int, nome: str, cpf: int, saldo: float = 0) -> None:
        if saldo < 0:
            raise ValueError("Não é possível criar uma conta com saldo negativo.")
        if type(numConta) != int:
            raise ValueError("O número da conta deve ser um valor inteiro.")
        if type(cpf) != int:
            raise ValueError("O número do CPF deve ser um valor inteiro.")
        self.__numeroConta = numConta
        self.__numeroAgencia = numAg
        self.__banco = banco
        self.__nomeTitular = nome
        self.__cpfTitular = cpf
        self.__saldo = saldo

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser um número positivo.")
        if valor > self.__saldo:
            raise ValueError("O valor sacado não pode ser maior que o saldo disponível.")
        self.__saldo -= valor
        print(f"Você sacou R${valor}")

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser um número positivo.")
        self.__saldo += valor
        print(f"Você depositou R${valor}")

    def receber(self, valor: float):
        self.__saldo += valor

    def getSaldo(self) -> float:
        return self.__saldo
    
    def transferir(self, valor: float, conta) -> None:
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser um número positivo.")
        if valor > self.__saldo:
            raise ValueError("O valor transferido deve ser menor ou igual ao saldo da conta.")
        self.__saldo -= valor
        conta.receber(valor)
        print(f"Você transferiu R${valor} para a conta {conta}")

    def compraDebito(self, valor):
        if valor <= 0:
            raise ValueError("O valor da compra deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("O valor da compra não pode exceder o saldo disponível.")
        self.__saldo -= valor
        print(f"Compra no débito no valor de R${valor} realizada.")

    def __str__(self) -> str:
        return str(self.__numeroConta)


'''
conta1 = Conta()
conta2 = Conta()
conta1.transferir(valor, conta2)

conta1 = Conta(123, 123,123,"Rafael", 123)
conta2 = Conta(124, 123,123,"Alex", 124)

conta1.depositar(5)
conta1.transferir(5,conta2)
'''