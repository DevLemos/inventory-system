import unittest
from estoque import Estoque, Produto

class TestEstoque(unittest.TestCase):

    def setUp(self):
        self.estoque = Estoque()
        self.produto1 = Produto(codigo=1, nome="Maca", quantidade= 10, preco= 2.71)
        self.produto2 = Produto(codigo=2, nome="Pera", quantidade= 20, preco= 3.39)
        self.produto3 = Produto(codigo=3, nome="Laranja", quantidade= 50, preco= 5.39)
        self.produto4 = Produto(codigo=4, nome="Banana Prata", quantidade= 25, preco= 1.68)
    
    def test_adicionar_produto(self):
        self.estoque.adicionar_produto(self.produto1)
        self.assertIn(self.produto1.codigo, self.estoque.produtos)
        self.assertEqual(self.estoque.produtos[self.produto1.codigo], self.produto1)

        # Testa adicionar um produto com código duplicado
        with self.assertRaises(ValueError):
            self.estoque.adicionar_produto(self.produto1)

    def test_remover_produto(self):
        self.estoque.adicionar_produto(self.produto1)
        self.estoque.remover_produto(self.produto1.codigo)
        self.assertNotIn(self.produto1.codigo, self.estoque.produtos)

        # Testa remover um produto que não existe
        with self.assertRaises(KeyError):
            self.estoque.remover_produto(999)
        
    def test_consultar_produto(self):
        self.estoque.adicionar_produto(self.produto1)
        produto = self.estoque.consultar_produto(self.produto1.codigo)
        self.assertEqual(produto, self.produto1)

        # Testa consultar um produto que não existe
        with self.assertRaises(KeyError):
            self.estoque.consultar_produto(999)
        
    def test_listar_produtos(self):
        # Testa listar produtos em um estoque vazio
        self.assertEqual(self.estoque.listar_produtos(), [])

        # Testa listar produtos após adicionar alguns produtos
        self.estoque.adicionar_produto(self.produto1)
        self.estoque.adicionar_produto(self.produto2)
        produtos = self.estoque.listar_produtos()
        self.assertIn(self.produto1, produtos)
        self.assertIn(self.produto2, produtos)
    
    def test_atualizar_quantidade(self):
        self.estoque.adicionar_produto(self.produto1)
        self.estoque.atualizar_quantidade(self.produto1.codigo, 35)
        self.assertEqual(self.estoque.produtos[self.produto1.codigo].quantidade, 35)

        with self.assertRaises(KeyError):
            self.estoque.atualizar_quantidade(999, 20)  # Produto inexistente
        
        with self.assertRaises(ValueError):
            self.estoque.atualizar_quantidade(self.produto1.codigo, -10)  # Quantidade negativa

    def test_salvar_e_carregar_arquivo(self):
        # Salva o estoque em arquivo
        self.estoque.adicionar_produto(self.produto1)
        self.estoque.adicionar_produto(self.produto2)
        self.estoque.adicionar_produto(self.produto3)
        self.estoque.adicionar_produto(self.produto4)
        self.estoque.salvar_em_arquivo("estoque_teste.json")
        
        # Cria um novo estoque e carrega do arquivo
        novo_estoque = Estoque()
        novo_estoque.carregar_arquivo("estoque_teste.json")
        
        self.assertIn(self.produto1.codigo, novo_estoque.produtos)
        self.assertEqual(novo_estoque.produtos[self.produto1.codigo].nome, self.produto1.nome)

        self.assertIn(self.produto2.codigo, novo_estoque.produtos)
        self.assertEqual(novo_estoque.produtos[self.produto2.codigo].nome, self.produto2.nome)

        self.assertIn(self.produto3.codigo, novo_estoque.produtos)
        self.assertEqual(novo_estoque.produtos[self.produto3.codigo].nome, self.produto3.nome)

        self.assertIn(self.produto4.codigo, novo_estoque.produtos)
        self.assertEqual(novo_estoque.produtos[self.produto4.codigo].nome, self.produto4.nome)

if __name__ == '__main__':
    unittest.main()