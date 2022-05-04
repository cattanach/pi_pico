import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_onboard.value(0)
        for i in range(2):
            led_external.toggle()
            utime.sleep(.1)
        
    else:
        led_onboard.value(1)
        led_external.value(0)

        
