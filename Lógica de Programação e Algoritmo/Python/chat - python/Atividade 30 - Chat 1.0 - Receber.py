from click import clear
import time

while True:
    clear()
    with open("chat_1.txt", "r") as arquivo:
        mensagens = arquivo.readline()

    for mensagem in reversed(mensagens):
        print(mensagem)
    time.sleep(3)

