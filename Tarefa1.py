from bd import produtos

class ListadeProdutos:

    def adicionar_produto():
        nome_produto = input('Nome do produto:')
        produtos.append({
            '_id': ListadeProdutos.find_id(),
            'nome': nome_produto,
            'marca': input('Marca:'),
            'preco': input('Preço:')
        })

        print('Produto {} adicionado'.format(nome_produto))

    def adicionar_varios_produtos(self,numero):
        for i in range(0,numero):
            ListadeProdutos.adicionar_produto()

    def find_id(): #Procura o ID mais baixo disponivel
        used_id = []
        for i in range(len(produtos)):
            used_id.append(produtos[i].get('_id'))
        id = 1
        while id in used_id:
            id += 1
        return id

    def mostrar_todos_produtos(self):
        print(produtos)

    def procurar_produto_nome(self,nome):
        for i in range(len(produtos)):
            if nome == produtos[i].get('nome'):
                print(produtos[i])
                return
        print('Produto {} não encontrado.'.format(nome))

    def excluir_produto_nome(self,nome):
        for i in range(len(produtos)):
            if nome == produtos[i].get('nome'):
                produtos.pop(i)
                print('Produto {} excluido.'.format(nome))
                return
        print('Produto {} não encontrado'.format(nome))



lista1 = ListadeProdutos()
lista1.procurar_produto_nome('LoL')