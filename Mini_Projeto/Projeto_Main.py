#Projeto_Main.py
from Projeto_Cliente import cliente
from Projeto_Produto import produto
from Projeto_Carrinho import carrinho


cliente_01 = cliente(nome = "Ricardo",id_cliente = 1,cidade = "Chapeco",endereco= "Boa Vista, 453")
print(cliente_01.getNome())
print(cliente_01.getId_Cliente())
print(cliente_01.getCidade())
print(cliente_01.getEndereco())

cliente_02 = cliente(nome = "Thalyta",id_cliente = 2,cidade = "Curitiba",endereco= "São Paulo II, 932")
print(cliente_02.getNome())
print(cliente_02.getId_Cliente())
print(cliente_02.getCidade())
print(cliente_02.getEndereco())

cliente_03 = cliente(nome = "Inacio",id_cliente = 3,cidade = "Sao Paulo",endereco= "Campos Gerais, 1122")
print(cliente_03.getNome())
print(cliente_03.getId_Cliente())
print(cliente_03.getCidade())
print(cliente_03.getEndereco())

produto_01 = produto(id_produto = 1, descricao = "Coca-Cola 2Lts",valor=5.99)
print(produto_01.getId_produto())
print(produto_01.getDescricao())
print(produto_01.getValor())

produto_02 = produto(id_produto = 2, descricao = "Picanha Kilo",valor=59.99)
print(produto_02.getId_produto())
print(produto_02.getDescricao())
print(produto_02.getValor())

produto_03 = produto(id_produto = 3, descricao = "Farofa 500g",valor=3.59)
print(produto_03.getId_produto())
print(produto_03.getDescricao())
print(produto_03.getValor())

produto_04 = produto(id_produto = 4, descricao = "Heineken 355ml",valor=2.99)
print(produto_04.getId_produto())
print(produto_04.getDescricao())
print(produto_04.getValor())

produto_05 = produto(id_produto = 5, descricao = "Coxas de Frango Kilo",valor=8.00)
print(produto_05.getId_produto())
print(produto_05.getDescricao())
print(produto_05.getValor())

produto_06 = produto(id_produto = 6, descricao = "Coração de Frango",valor=15.99)
print(produto_06.getId_produto())
print(produto_06.getDescricao())
print(produto_06.getValor())

produto_07 = produto(id_produto = 7, descricao = "Limão Kilo",valor=4.20)
print(produto_07.getId_produto())
print(produto_07.getDescricao())
print(produto_07.getValor())

produto_08 = produto(id_produto = 8, descricao = "Cachaça Mineira 1Lt",valor=35.99)
print(produto_08.getId_produto())
print(produto_08.getDescricao())
print(produto_08.getValor())

produto_09 = produto(id_produto = 9, descricao = "Acucar 500g",valor=2.15)
print(produto_09.getId_produto())
print(produto_09.getDescricao())
print(produto_09.getValor())

carrinho_01 = carrinho(1,1,0,3,6,produto_01.valor,0)
print(carrinho_01.id_produto)
print(carrinho_01.id_cliente)
print(carrinho_01.adiccao)
print(carrinho_01.exclusao)
print(carrinho_01.quantidade)
print(carrinho_01.valor)
print(carrinho_01.valor_total)

#4 – Após a contrução das classes, execute as seguintes ações:

#    1. 4.1 – Crie dois ou mais objetos cliente, entre 4 ou 5 objetos produtos;
#    2. 4.2 – Adicione e remova itens do carrinho se atentando aos valores totais e a ligação entre produto e cliente;

#5 – No final das ações acima, exiba, todos os clientes criados, todos os produtos criados,
# todos os produtos do carrinho com os devidos produtos e clientes relacionados.
print(cliente_01.nome, cliente_02.nome, cliente_03.nome)

