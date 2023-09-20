import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.2)

colors = [[0,0,255],[255,0,0],[255,255,255]]
speed = 0.01
times = 50
i = 0
color = [0,0,255]
fOrange1 = (255,54,0)
fOrange2 = (255,74,0)
fOrange3 = (255,34,0)
red = (255,0,0)
black = (0,0,0)
fColors = [fOrange1,fOrange2,fOrange3,red,black]

def fire(colors, speed = 0.1):
    led = [random.randint(0,29) for i in range(30)]
    for i in led:
        delay = random.random()/2
        np[i] = colors[random.randint(0,4)]
        time.sleep(delay)
        np.show()
        print("fire",delay)

np.fill(red)
while True:
    fire(fColors)
