import time
import lcd2x16
import game
import buzzer
import lcd2x16
import led
# import os
import platform
import multiprocessing as mp
# import adafruit_character_lcd.character_lcd_i2c as _lcd

# hi
# led.blink


def main():
    # i = 0
    print("Hello World", platform.machine())
    if (platform.machine().lower() == "armv7l" or platform.machine().lower() == "arm64"):
        mp.Process(target=lcd2x16.lcdClock).start()
        mp.Process(target=buzzer.play).start()
        mp.Process(target=led.blink)
    game.run()

if __name__ == "__main__":
    print("Main")
    try:
        # main()
        main()
    except KeyboardInterrupt:
        print("closing")
        led.close()
        buzzer.stop()
        time.sleep(.75)
        lcd2x16.close()
        game.close()
