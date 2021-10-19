import unittest
from main import insere_dados

teste = insere_dados()


class MyTestCase(unittest.TestCase):

    def testa_nome_vazio(self):
        self.assertFalse(teste.Nome == "", "Nome em branco")

    def testa_nome_inicia_com_maiuscula(self):
        self.assertTrue(teste.Nome[0].isupper(), "Nome não inicia com maiúscula")

    def testa_idade_maior_ou_igual_a_zero(self):
        self.assertGreaterEqual(teste.Idade, 0, "Idade menor que zero")

    def testa_sexo_eh_M_ou_F(self):
        self.assertTrue(teste.Sexo.__eq__("M") or teste.Sexo.__eq__("F"), "Sexo não é M ou F")

    def testa_cidade_vazio(self):
        self.assertFalse(teste.Cidade == "", "Nome em branco")

    def testa_cidade_inicia_com_maiuscula(self):
        self.assertTrue(teste.Cidade[0].isupper(), "Cidade com inicial minúscula")

    def testa_estado_vazio(self):
        self.assertFalse(teste.Estado == "", "Estado em branco")

    def testa_estado_maiusculo(self):
        self.assertTrue(teste.Estado.isupper(), "Estado em minúsculo")

    def testa_estado_com_duas_letras(self):
        self.assertEqual(len(teste.Estado), 2, "Estado não tem duas letras")


if __name__ == '__main__':
    unittest.main()
