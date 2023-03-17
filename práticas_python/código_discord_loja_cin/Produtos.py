class Produto():
    __nome = ""
    __preco = 0

    def __init__(self, nome: str, preco: float) -> None:
        self.__nome = nome
        self.__preco = preco

    def setPreco(self, novoPreco):
        self.__preco = novoPreco

    def getPreco(self) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f"Produto: {self.__nome}\tPreço: R${self.__preco}"
    
    def __repr__(self) -> str:
        return str(self)