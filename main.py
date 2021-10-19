Nome = ""
Idade = None
Sexo = ''
Cidade = ""
Estado = ""


def insere_dados():
    Nome = str(input("Digite seu nome: "))
    Idade = int(input("Digite sua idade: "))
    Sexo = str(input("Digite seu sexo (M ou F): ")).upper()
    Cidade = str(input("Digite sua cidade: "))
    Estado = str(input("Digite seu estado (ex. CE): ")).upper()


if __name__ == "__main__":
    insere_dados()
