import machine
import time 

gremio = machine.Pin(12, machine.Pin.OUT)
gremio1983 = machine.Pin(14, machine.Pin.OUT)
gremio2008 = machine.Pin(27, machine.Pin.OUT)


while True:
  gremio.value(1)
  time.sleep(5)
  gremio.value(0)
  
  gremio1983.value(1)
  time.sleep(1)
  gremio1983.value(0)
  
  
  gremio2008.value(1)
  time.sleep(3)
  gremio2008.value(0)
  
  


