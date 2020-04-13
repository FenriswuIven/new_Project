#Projeto_Produto.py

#2 – Crie uma classe produto, contendo id do produto, descrição do produto e valor do produto;
class produto:
    def __init__(self, id_produto, descricao, valor):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor

    def setId_produto (self, id_produto):
        self.id_produto = id_produto
    
    def setDescricao (self, descricao):
        self.descricao = descricao
    
    def setValor (self, valor):
        self.valor = valor

    def getId_produto (self):
        return self.id_produto

    def getDescricao (self):
        return self.descricao

    def getValor (self):
        return self.valor
