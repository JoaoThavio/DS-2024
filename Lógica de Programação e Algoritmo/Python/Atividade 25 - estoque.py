from click import clear
letra = 's'

escolha = 0

nomep = []
valorp = []
des = []
quant = []

def adicionar():

    clear()
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nomep.append(nome)
    valorp.append(valor)
    des.append(descricao)
    quant.append(quantidade)

    with open("Dados do produto", 'a') as arquivos:
        arquivos.write(f'{nome}, {valor}, {descricao}, {quantidade}\n')

    letra = input('Deseja continuar? [s/n]: ')

clear()

def mostrar():

    opcao = input('Deseja exibir os produtos [s/n]')
    if opcao == 's':
        print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(nomep)):
        print(f'{nomep[i]} \t\t  {valorp[i]} \t\t\t  {quant[i]} \t\t= {des[i]}')
clear()

def remover():
    opcao_2 = input('Deseja deletar um produto? [s/n]: ')
    if opcao_2 == 's':
     dele = int(input("Digite qual deseja deletar: "))
    if dele == dele:
        nomep.pop(dele), valorp.pop(dele), quant.pop(dele), des.pop(dele)

def produtos_cadastrados():
    with open("Dados do produto", 'r') as arquivos:
        print("Produtos cadastadas: ")
        for linha in arquivos:
            nome, valor, descricao, quantidade = linha.strip().split(',')
            print(f'nome do produto: {nome}, Valor: {valor}, quantidade: {quantidade}, descrição: {descricao}\n')

while True:
    clear()

    print("Escolha uma opção")
    print("1 - Para adicionar um produto")
    print("2 - Para mostrar produtos")
    print("3 - Para excuir um produto")
    print("4 - Para ver produtos já no estoque")
    print("5 - Para fechar o programa")
    escolha = int(input("O que deseja fazer?: "))
    if escolha == 1:
        adicionar()
    elif escolha == 2:
        mostrar()
    elif escolha == 3:
        remover()
    elif escolha == 4:
        produtos_cadastrados()
    elif escolha == 5:
        break
