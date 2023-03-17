from Conta import Conta

class ContaCorrente(Conta):
    __limCredito = 0
    __credUtilizado = 0

    def __init__(self, numConta: int, numAg: int, banco: int, nome: str, cpf: int, credito: float = 0, saldo: float = 0) -> None:
        super().__init__(numConta, numAg, banco, nome, cpf, saldo)
        if credito < 0:
            raise ValueError("O limite de crédito não pode ser um valor negativo.")
        self.__limCredito = credito

    def compraCredito(self, valor: float) -> None:
        creditoDisponivel = self.__limCredito - self.__credUtilizado
        if valor <= 0:
            raise ValueError("O valor da compra deve ser positivo.")
        if valor > creditoDisponivel:
            raise ValueError("Você não tem crédito para realizar essa compra.")
        self.__credUtilizado += valor
        print(f"Compra no crédito no valor de R${valor} realizada.")

    def pagarFatura(self, valorPago: float) -> None:
        if valorPago <= 0:
            raise ValueError("O valor da fatura paga deve ser positivo.")
        if valorPago > self.__credUtilizado:
            raise ValueError("O valor pago na fatura deve ser menor ou igual ao crédito utilizado.")
        self.__credUtilizado -= valorPago
        print(f"Você realizou o pagamento da fatura no valor de R${valorPago}")
        print(f"Você tem um crédito disponível de R${self.__limCredito - self.__credUtilizado}")

    def getCreditoDisponivel(self) -> float:
        return self.__limCredito - self.__credUtilizado


'''conta1 = ContaCorrente(123, 123, 123, "Rafael", 123, 1000, 200)
print(conta1.getSaldo())
#conta1.compraDebito(300)
conta1.compraDebito(100)
print(conta1.getSaldo())

conta1.compraCredito(575)
conta1.pagarFatura(500)

conta1.compraCredito(1200)'''

