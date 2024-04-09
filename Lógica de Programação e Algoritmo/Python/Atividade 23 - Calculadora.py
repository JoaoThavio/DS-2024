letra = 's'

while letra == 's':

    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))

    print('[1] = Adição')
    print('[2] = Subtração')
    print('[3] = Multiplicacao')
    print('[4] = Divisão')
    v3 = str(input('Digite a qual operação deseja realizar: '))

    if v3 == '1':
        print('resultado =',v1 + v2)
    elif v3 == '2':
        print('resultado =',v1 - v2)
    elif v3 == '3':
        print('resultado =',v1 * v2)
    elif v3 == '4':
        print('resultado =',v1 / v2)

    letra = input('Deseja realizar um novo calculo? [s/n]: ')
