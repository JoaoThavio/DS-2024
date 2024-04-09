from click import clear

nome = str(input('Digite seu nome: '))
idade = str(input('Digite a sua idade:'))
email = str(input('Digite seu email: '))
data =  str(input('Digite sua Data de nascimento: '))
telefone = str(input('Digite seu Telefone: '))


clear()

print(f"Nome da pessoa: {nome}")
print(f"Idade: {idade}")
print(f"E-mail: {email}")
print (f"Telefone: {telefone}")
print (f"Data de Nascimento: {data}")