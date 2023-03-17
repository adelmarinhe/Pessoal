from Produtos import Produto

class Controle():
    __estoque = {} # Dicionario que vai armazenar os produtos

    def cadastro(self, produto: str, preco: float, quantidade: int = 0):
        if quantidade < 0:
            raise ValueError("A quantidade em estoque não pode ser negativa")
        if int(quantidade) != quantidade:
            raise ValueError("A quantidade deve ser um número inteiro")
        if preco <= 0:
            raise ValueError("O valor do produto deve ser positivo")
        if produto in self.__estoque:
            raise ValueError("O produto já está cadastrado")
        self.__estoque[produto] = [Produto(produto, preco), quantidade]
        # Cada registro do dicionario é uma lista com o produto e a quantidade em estoque
        
    def saida(self, produto: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser um número positivo")
        if int(quantidade) != quantidade: # type(quantidade) != int
            raise ValueError("A quantidade deve ser um número inteiro")
        if produto not in self.__estoque:
            raise ValueError("O produto não está cadastrado no estoque")
        elif quantidade > self.__estoque[produto][1]:
            raise ValueError("Não é possivel retirar uma quantidade maior do que há em estoque")
        self.__estoque[produto][1] -= quantidade

    def entrada(self, produto: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser um número positivo")
        if int(quantidade) != quantidade:
            raise ValueError("A quantidade deve ser um número inteiro")
        if produto not in self.__estoque:
            raise ValueError("O produto não está cadastrado no estoque")
        self.__estoque[produto][1] += quantidade

    def listarProdutosDisponiveis(self):
        if len(self.__estoque) == 0:
            print("Não há nenhum produto cadastrado")
        for produto in self.__estoque:
            if self.__estoque[produto][1] > 0:
                print(self.__estoque[produto][0])

    def listarProdutosIndisponiveis(self):
        if len(self.__estoque) == 0:
            print("Não há nenhum produto cadastrado")
        for produto in self.__estoque:
            if self.__estoque[produto][1] == 0:
                print(self.__estoque[produto][0])

    def alterarPreco(self, produto: str, novoValor: float):
        if produto not in self.__estoque:
            raise ValueError("Produto não cadastrado")
        if novoValor <= 0:
            raise ValueError("O valor do produto deve ser positivo")
        self.__estoque[produto][0].setPreco(novoValor)

    def getValor(self, produto: str) -> float:
        return self.__estoque[produto][0].getPreco()