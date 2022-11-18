import time
import random
class Nuller():
    def off(self):
        None

_led = Nuller()

def blink():
    global _led
    import gpiozero
    led = gpiozero.LED(23)
    _led = led
    # return
    i = 0
    # led.on()
    while (True):
        i+=1
        led.on()
        # print(led.is_active)
        time.sleep(random.random())
        #sleep(.5)
        led.off()
        #sleep(.5)
        time.sleep(random.random())
        print(f"{i} blinks")
        None

def close():
    _led.off()
