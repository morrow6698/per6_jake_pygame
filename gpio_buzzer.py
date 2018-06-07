from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(16)

while True:
    buzzer.beep()
    sleep(0.1)
    buzzer.off()
    
