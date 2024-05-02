import machine 
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(23))
botao = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
gremio = machine.Pin(14, machine.Pin.OUT)
gremio1983 = machine.Pin(12, machine.Pin.OUT)

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True: 
    blue = botao.value()
    red = botao2.value()

    if blue == 0:
        gremio.value(0), gremio1983.value(1)
        tela.fill(0)
        tela.text('A umidade da', 0, 0)
        tela.text('sala e: 2017', 0, 10)
        tela.show()
   
    if red == 0:
         gremio.value(1), gremio1983.value(0)
         tela.fill(0)
         tela.text('A temperatura', 0, 0)
         tela.text('da sala e: 2016', 0, 10)
         tela.text('graus', 0, 20)
         tela.show()
    