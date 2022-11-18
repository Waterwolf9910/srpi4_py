import time

class Nuller():
    def stop():
        None

_buzzer = Nuller()

def play():
    global _buzzer
    import gpiozero
    from gpiozero.tones import Tone
    buzzer = gpiozero.TonalBuzzer(19)
    _buzzer = buzzer
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

def close():
    _buzzer.stop()
