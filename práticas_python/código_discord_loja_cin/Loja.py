from ControleEstoque import Controle

class Loja():
    __estoque = Controle()
    __caixa = 0

    def cadastrarNovoProduto(self, produto: str, preco: float, quantidade: int) -> None:
        try:
            self.__estoque.cadastro(produto, preco, quantidade)
        except Exception as erro:
            print(erro)

    def editarPreco(self, produto:str, novoPreco: float) -> None:
        try:
            self.__estoque.alterarPreco(produto, novoPreco)
        except Exception as erro:
            print(erro)

    def venda(self, produto: str, quantidade: int) -> None:
        try:
            self.__estoque.saida(produto, quantidade)
            self.__caixa += self.__estoque.getValor(produto)*quantidade
        except Exception as erro:
            print(erro)

    def abastecerProduto(self, produto: str, quantidade: int) -> None:
        try:
            self.__estoque.entrada(produto, quantidade)
        except Exception as erro:
            print(erro)

    def printarLoja(self) -> None:
        print("Produtos disponiveis:\n")
        self.__estoque.listarProdutosDisponiveis()
        print("\nProdutos em falta:\n")
        self.__estoque.listarProdutosIndisponiveis()

    def ganhos(self) -> float:
        return self.__caixa