import pygame
import convert

class GConf:

    def __init__(this) -> None:
        pygame.init()
        this.baseFont = pygame.font.Font(None, 18)
        this.screen = pygame.display.set_mode(this.size)
        this.inputWindow = pygame.Rect((this.width-this.rectWidth)/2, (this.height-this.rectHeight)/2, this.rectWidth, this.rectHeight)
        this.clock = pygame.time.Clock()

    start = False
    FPS = 60
    clock: pygame.time.Clock
    size = width, height = 1280, 720
    screen: pygame.surface.Surface
    baseFont: pygame.font.Font
    r = 168
    g = 50
    b = 50
    uinput = ""
    rectWidth = 200
    rectHeight = 200
    inputWindow: pygame.Rect
    inputSelected = False

gconfig: GConf

def quit(code = 0):
    pygame.quit()
    exit(code)

def onMouseDown(event: pygame.event.Event): #Mouse Click Events
    global gconfig
    if (gconfig.inputWindow.collidepoint(event.pos)):
        gconfig.inputSelected = True
    else:
        gconfig.inputSelected = False

def onKeyDown(event: pygame.event.Event): #Keyboard Click Events
    global gconfig
    if (gconfig.inputSelected):
        if (event.key == pygame.K_BACKSPACE):
            gconfig.uinput = gconfig.uinput[:-1]
        elif (event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9):
            gconfig.uinput += event.unicode
        elif (event.key == pygame.K_ESCAPE):
            gconfig.uinput = ""
        elif (event.key == pygame.K_RETURN):
            print(f"in: {convert.cmToIn(int(gconfig.uinput))}")
            print(f"cm: convert.inToCM(int(gconfig.uinput))")
    if (event.key == pygame.K_SPACE and not gconfig.start):
        gconfig.r = 168
        gconfig.g = 50
        gconfig.b = 50
        gconfig.start = True

def checkEvents(): # Event Handler to Call Sub Handlers
    global gconfig
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            onMouseDown(event)
        if (event.type == pygame.KEYDOWN):
            onKeyDown(event)

def setColors(): #Setting Colors for Screen and other objects
    global gconfig
    if (gconfig.r == 168 and gconfig.g < 168 and gconfig.b == 50 and gconfig.g < 168):
        gconfig.g = gconfig.g+1
    elif (gconfig.g == 168 and gconfig.b == 50 and gconfig.r <= 168 and gconfig.r > 50):
        gconfig.r = gconfig.r-1
    elif (gconfig.g == 168 and gconfig.r == 50 and gconfig.b >= 50 and gconfig.b < 168):
        gconfig.b = gconfig.b+1
    elif (gconfig.b == 168 and gconfig.r == 50 and gconfig.g <= 168 and gconfig.g > 50):
        gconfig.g = gconfig.g-1
    elif (gconfig.r >= 50 and gconfig.g == 50 and gconfig.b == 168 and gconfig.r < 168):
        gconfig.r = gconfig.r+1
    elif (gconfig.r == 168 and gconfig.g == 50 and gconfig.b <= 168 and gconfig.b > 50):
        gconfig.b = gconfig.b-1

def render():
    global gconfig
    pygame.draw.rect(gconfig.screen, (255, 255, 255), gconfig.inputWindow)
    text = gconfig.baseFont.render(gconfig.uinput, True, (0, 0, 0))
    gconfig.screen.blit(text, (gconfig.inputWindow.x+5, gconfig.inputWindow.y+5))
    gconfig.inputWindow.w = max(gconfig.rectWidth, text.get_width()+10)
    _rectHPos = (gconfig.width-gconfig.rectWidth)/2
    txtW = (text.get_width() + 10)
    if (txtW > gconfig.rectWidth):
        gconfig.inputWindow.left = (gconfig.width-txtW)/2
    else:
        gconfig.inputWindow.left = _rectHPos
    pygame.display.flip()
    gconfig.screen.fill((gconfig.r, gconfig.g, gconfig.b))


def run():
    global gconfig

    gconfig = GConf()

    while (True):

        checkEvents()
        if (gconfig.start):
            setColors()
            render()

        gconfig.clock.tick(gconfig.FPS)

def close(code = 0):
    quit(code)
