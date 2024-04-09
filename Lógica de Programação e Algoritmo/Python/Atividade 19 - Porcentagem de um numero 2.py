letra = 's'
while letra == 's':

    valor = float(input('Digite o valor que deseja calcular: '))
    porcentagem = float(input('Digite da porcentagem que quer: '))

    soma = valor * porcentagem/100

    print(f"O valor será: {soma}")

    letra = input('Deseja fazer um novo lançamento? [s/n]: ')
