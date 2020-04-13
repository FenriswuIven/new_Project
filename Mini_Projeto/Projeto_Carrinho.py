#Projeto_Carrinho.py
from Projeto_Cliente import cliente
from Projeto_Produto import produto

#3 – Crie uma classe carrinho, que tenha métodos de adicionar e deletar produtos do carrinho, 
#lembrando de guardar no carrinho o id do cliente e do produto, além da quantidade adicionada, valor do produto e valor total;
class carrinho:
    def __init__(self, id_produto, id_cliente
                , adiccao, exclusao, quantidade, valor, valor_total):
        self.id_produto = id_produto
        self.id_cliente = id_cliente
        self.adiccao = adiccao
        self.exclusao = exclusao
        self.quantidade = quantidade + adiccao - exclusao
        self.valor = valor
        self.valor_total = valor*self.quantidade

    def setId_produto(self,id_produto):
        produto.id_produto = id_produto

    def getId_produto(self):
        return produto.id_produto

    def setId_Cliente(self,id_cliente):
        cliente.id_cliente = id_cliente

    def getId_Cliente(self):
        return cliente.id_cliente
    
    def setAdiccao(self,adiccao):
        self.adiccao = adiccao

    def getAdiccao(self):
        return self.adiccao

    def setExclusao(self,exclusao):
        self.exclusao = exclusao

    def getExclusao(self):
        return self.exclusao

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
    
    def setValor(self,valor):
        self.valor = valor

    def getValor (self, valor):
        return self.valor

    def setValor_Total(self, valor_total):
        self.valor_total = valor_total

    def getValor_Total (self):
         return self.valor_total




    




