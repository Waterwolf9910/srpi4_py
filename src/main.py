import time
import datetime
import pygame
import random
import os
import gpiozero
import board
import digitalio
import adafruit_character_lcd.character_lcd_i2c as _lcd

led = gpiozero.LED(23)
# hi
# led.blink
def main():
    # i = 0
    a = os.fork()
    if (a != 0):
        print("Hello World")
        lcd = _lcd.Character_LCD_I2C(board.I2C(), 16, 2, 27)
        lcd.clear()
        time.sleep(3)
        lcd.cursor = True
        lcd.blink = True
        shown = False
        colon = shown ? ":": ""
        while (True):
            dtime = time.strftime(f"%H{}%S")
            lcd.clear()
            time.sleep(0.5)
            lcd.message = f"Time {dtime}"
            # if (i < 50):
            #     i+=1
            #     print(i)
            None
    else:
        blink()


def blink():
    i = 0
    while (True):
        i+=1
        led.on()
        time.sleep(random.random())
        #sleep(.5)
        led.off()
        #sleep(.5)
        time.sleep(random.random())
        print(f"{i} blinks")

if __name__ == "__main__":
    print("Main")
    main()
