import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_external = machine.Pin(15, machine.Pin.OUT)


for i in range(10):
    led_onboard.value(1)
    led_external.value(0)
    utime.sleep(.1)
    led_onboard.value(0)
    led_external.value(1)
    utime.sleep(.1)

while True:
    led_onboard.toggle()
    led_external.toggle()
    utime.sleep(1)