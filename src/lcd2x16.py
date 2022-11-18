import time

class Nuller():
    def clear(self):
        None

_lcd = Nuller()

def lcdClock():
    global _lcd
    import rpi_lcd
    lcd = rpi_lcd.LCD(0x27, 1, 16, 2)

    _lcd = lcd
    # lcd = _lcd.Character_LCD_I2C(board.I2C(), 16, 2, 0x27)
    # time.sleep(3)
    lcd.clear()
    time.sleep(1)
    # lcd.cursor = True
    # lcd.blink = True
    # lcd.backlight = True
    lcd.backlight(True)
    shown = False
    # return
    while (True):
        # lcd.clear()
        colon = " "
        if (shown):
            colon = ":"
        dtime = time.strftime(f"%H{colon}%M")
        lcd.text(f"Time {dtime}", 1)
        lcd.text(f"Hello World! :3", 2)
        # lcd.clear()
        # lcd.cursor_position(0, 0)
        # lcd.message = f"Time {dtime}\n"
        # lcd.cursor_position(0, 1)
        # lcd.message = f"M"
        time.sleep(0.5)
        # if (i < 50):
        #     i+=1
        #     print(i)
        shown = not shown


def close():
    time.sleep(1)
    _lcd.clear()
