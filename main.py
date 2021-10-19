from Pessoa import Pessoa


def insere_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M ou F): ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu estado (ex. CE): ")
    return Pessoa(nome, idade, sexo, cidade, estado)


if __name__ == "__main__":
    insere_dados()
