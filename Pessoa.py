class Pessoa:

    def __init__(self, nome, idade, sexo, cidade, estado):
        self.Nome = str(nome).capitalize()
        self.Idade = idade
        self.Sexo = str(sexo).upper()
        self.Cidade = str(cidade).capitalize()
        self.Estado = str(estado).upper()
