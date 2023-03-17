from Loja import Loja

lojinhaDoCIn = Loja()

'''lojinhaDoCIn.cadastrarNovoProduto("Coxinha", 5.0, 15)
lojinhaDoCIn.cadastrarNovoProduto("Bomba", 500.0, 5)
lojinhaDoCIn.cadastrarNovoProduto("Xbox", 20, 2)

lojinhaDoCIn.printarLoja()

lojinhaDoCIn.venda("Lapis", 1)
lojinhaDoCIn.venda("Bomba", 10)
lojinhaDoCIn.venda("Coxinha", 15)

lojinhaDoCIn.printarLoja()

print(lojinhaDoCIn.ganhos())'''

lojinhaDoCIn.cadastrarNovoProduto("Lapis", 2, 0)

lojinhaDoCIn.venda("Lapis", 1)

lojinhaDoCIn.abastecerProduto("Lapis", 10)

lojinhaDoCIn.venda("Lapis", 5)

print(lojinhaDoCIn.ganhos())