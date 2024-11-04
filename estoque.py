import json

class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def  __repr__(self):
        return f'Produto(codigo = {self.codigo}, nome = {self.nome}, quantidade = {self.quantidade}, preco = {self.preco})' 

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.codigo in self.produtos:
            raise ValueError("Produto já cadastrado no estoque")
        self.produtos[produto.codigo] = produto
    
    def remover_produto(self, codigo):
        if codigo not in self.produtos:
            raise KeyError("Produto não encontrado no estoque")
        del self.produtos[codigo]
    
    def consultar_produto(self, codigo):
        if codigo not in self.produtos:
            raise KeyError("Produto não encontrado no estoque")
        return self.produtos[codigo]
    
    def listar_produtos(self):
        return list(self.produtos.values())

    def atualizar_quantidade(self, codigo, nova_quantidade):
        if codigo not in self.produtos:
            raise KeyError("Produto não encontrado no estoque")
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")
        self.produtos[codigo].quantidade = nova_quantidade

    def salvar_em_arquivo(self, nome_arquivo="estoque.json"):
        dados = {codigo: vars(produto) for codigo, produto in self.produtos.items()}
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("Estoque salvo em arquivo.")

    def carregar_arquivo(self, nome_arquivo="estoque.json"):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                for codigo, dados_produto in dados.items():
                    produto = Produto(
                        codigo=int(codigo),
                        nome=dados_produto['nome'],
                        quantidade=dados_produto['quantidade'],
                        preco=dados_produto['preco']
                    )
                    self.produtos[int(codigo)] = produto 
            print("Estoque carregado do arquivo.")
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. Um novo será criado ao salvar.")

