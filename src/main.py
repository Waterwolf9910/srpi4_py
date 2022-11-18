import time
import datetime
import pygame
import random
import os
import gpiozero
from gpiozero.tones import Tone
import rpi_lcd
import convert
# import adafruit_character_lcd.character_lcd_i2c as _lcd

led = gpiozero.LED(23)
buzzer = gpiozero.TonalBuzzer(19)
# hi
# led.blink
lcd = rpi_lcd.LCD(0x27, 1, 16, 2)

def game():
    pygame.init()

    start = False
    FPS = 60
    clock = pygame.time.Clock()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    baseFont = pygame.font.Font(None, 18)
    r = 168
    g = 50
    b = 50

    input = ""
    rectWidth = 200
    rectHeight = 200
    inputWindow = pygame.Rect(rectWidth, rectHeight, (width-rectWidth)/2, 50)
    inputSelected = False

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (inputWindow.collidepoint(event.pos)):
                    inputSelected = True
                else:
                    inputSelected = False
            if (event.type == pygame.KEYDOWN):
                if (inputSelected):
                    if event.key == pygame.K_BACKSPACE:
                        input = input[:-1]
                    elif event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                        input += event.unicode
                if event.key == pygame.K_SPACE:
                    r = 168
                    g = 50
                    b = 50
                    start = True

        if (start):
            if (r == 168 and g < 168 and b == 50 and g < 168):
                g = g+1
            elif (g == 168 and b == 50 and r <= 168 and r > 50):
                r = r-1
            elif (g == 168 and r == 50 and b >= 50 and b < 168):
                b = b+1
            elif (b == 168 and r == 50 and g <= 168 and g > 50):
                g = g-1
            elif (r >= 50 and g == 50 and b == 168 and r < 168):
                r = r+1
            elif (r == 168 and g == 50 and b <= 168 and b > 50):
                b = b-1
            pygame.draw.rect(screen, (255, 255, 255), inputWindow)
            text = baseFont.render(input, True, (0, 0, 0))
            screen.blit(text, (inputWindow.x+5, inputWindow.y+5))
            inputWindow.w = max(100, text.get_width()+10)
            pygame.display.flip()
        screen.fill((r, g, b))

        clock.tick(FPS)

def lcdClock():
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

def play():
    i = 60.0
    reverse = False
    while (True):
        if (i > 81.0):
            i = 80.0
            reverse = True
        elif (i < 60.0):
            reverse = False
            i = 61.0
        buzzer.play(i)
        if (reverse):
            i = i-1
        else:
            i = i+1
        time.sleep(0.3)
        buzzer.stop()
        # print(i)

def main():
    # i = 0
    a = os.fork()
    if (a != 0):
        print("Hello World")
        b = os.fork()
        if (b != 0):
            c = os.fork()
            if (c != 0):
                blink()
            else:
                game()
        else:
            play()
    else:
        lcdClock()
        None

def blink():
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

if __name__ == "__main__":
    print("Main")
    try:
        # main()
        game()
    except KeyboardInterrupt:
        print("closing")
        buzzer.stop()
        time.sleep(.75)
        lcd.clear()
        exit(0)
