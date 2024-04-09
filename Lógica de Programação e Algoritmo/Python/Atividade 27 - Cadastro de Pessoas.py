from click import clear


def adicionar_pessoas():
    nome = input('Digite o nome da pessoa: ')
    email = input('Digite o email da pessoa: ')

    with open("pessoas.txt", 'a') as arquivos:
        arquivos.write(f'{nome},{email}\n')

    print("pessoas cadastradas com suscesso!!")

def listar_pessoas():
    with open("pessoas.txt", 'r') as arquivos:
        print("pessoas cadastadas: ")
        for linha in arquivos:
            nome, email = linha.strip().split(',')
            print(f'nome: {nome}, email: {email}\n')

#adicionar_pessoas()
listar_pessoas()