#nesse caso o novo domínio que eu fiz seria uma loja.

#classes

#DIAGRAMA DE CLASSES:
#┌────────────────────────┐
#│        Pessoa          │
#├────────────────────────┤
#│ - _nome                │
#│ - _idade               │
#│ - _profissao           │
#│ - _salario             │
#├────────────────────────┤
#│ + get_nome()           │
#│ + set_nome()           │
#| + get_idade()          │
#│ + set_idade()          │
#│ + get_profissao()      │
#│ + set_profissao()      │
#│ + get_salario()        │
#│ + set_salario()        │
#└───────────▲────────────┘
#            │
#            │ utiliza
#            │
#┌───────────┴────────────┐
#│        Calcula         │
#├────────────────────────┤
#│ - _qtd                 │
#│ - _total1              │
#│ - _total2              │
#├────────────────────────┤
#│ - _media_sal()         │
#│ - _media_idade()       │
#└────────────────────────┘
class Produto:

    def __init__(self, nome, preco=0, estoque=0):
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_estoque(estoque)

    #getter e setter do nome
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    #getter e setter do preço
    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self._preco = preco

    #getter e setter do estoque
    def get_estoque(self):
        return self._estoque

    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self._estoque = estoque


class Carrinho:

    def __init__(self):
        self._qtd = 0

    #calcula a média dos preços dos produtos
    def _media_preco(self, p1, p2):
        self._qtd += 1
        self._media = (p1.get_preco() + p2.get_preco()) / 2
        return self._media

    # verifica se o produto está disponível
    def _verificar_estoque(self, produto):
        self._qtd += 1

        if produto.get_estoque() > 0:
            return "Produto disponível."
        else:
            return "Produto sem estoque."


# main
if __name__ == "__main__":

    #aqui é a primeira forma de criação onde todos os valores são informados.
    produto1 = Produto("Teclado", 150, 10)

    #aqui apenas o nome é informado.
    produto2 = Produto("Mouse")

    #print das informações dos produtos.
    print("Produto 1:")
    print("Nome:", produto1.get_nome())
    print("Preço:", produto1.get_preco())
    print("Estoque:", produto1.get_estoque())

    print("\nProduto 2:")
    print("Nome:", produto2.get_nome())
    print("Preço:", produto2.get_preco())
    print("Estoque:", produto2.get_estoque())

    #cria objeto da classe Carrinho
    carrinho = Carrinho()

    #calcula a média dos preços dos produtos.
    print(
        "\nMédia dos preços:",
        carrinho._media_preco(produto1, produto2)
    )

    #verifica se o produto 1 está disponível.
    print(
        "Estoque do produto 1:",
        carrinho._verificar_estoque(produto1)
    )

    #teste de exceção para preço negativo
    try:
        produto3 = Produto("Monitor", -500, 5)
    except ValueError as erro:
        print("\nCriação recusada:", erro)

    #teste de exceção para estoque negativo.
    try:
        produto4 = Produto("Celular", 1000, -3)
    except ValueError as erro:
        print("Criação recusada:", erro)


# AUTOAVALIAÇÃO:

#Critérios atingidos durante a atividade: todos

#Trecho que mais deu trabalho: entender como mostrar o diagrama de classes

# Uso de IA:
#utilizada para auxiliar na organização do código,
#identificação de possíveis erros e elaboração do diagrama de classes.