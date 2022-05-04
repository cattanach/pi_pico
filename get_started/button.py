import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("beep")
        utime.sleep(.25)
    else:
        print("boop")
        utime.sleep(.25)
        
