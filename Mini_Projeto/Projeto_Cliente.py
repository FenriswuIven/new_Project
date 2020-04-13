#Projeto_Cliente.py

#Mini-Projeto carrinho de compras:

#1 – Crie uma classe cliente, contendo nome do cliente, id do cliente, cidade e endereço;
class cliente:
    def __init__(self, nome, id_cliente, cidade, endereco):
        self.nome = nome
        self.id_cliente = id_cliente
        self.cidade = cidade
        self.endereco = endereco

    def setNome (self, nome):
            self.nome = nome
    
    def setId_cliente ( self, id_cliente):
            self.id_cliente = id_cliente
    
    def setCidade (self, cidade):
            self.cidade = cidade
    
    def setEndereco (self, endereco):
            self.endereco = endereco
    
    def getNome (self):
        return self.nome
    
    def getId_Cliente (self):
        return self.id_cliente
    
    def getCidade (self):
        return self.cidade

    def getEndereco (self):
        return self.endereco





