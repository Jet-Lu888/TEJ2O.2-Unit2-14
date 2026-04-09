"""
Created by: Jet Lu
Created on: Apr 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *

# start
display.show(Image.HAPPY)

# variables
loopCounterY= 0
loopCounterX= 0

while True :
    if button_a.was_pressed() :
        display.clear()
        loopCounterY= 0
        loopCounterX= 0

        # move pixel
        while (loopCounterX <= 4) :
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX += 1
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)

        # move pixel down
        while (loopCounterY <= 4) :
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY += 1
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)

        # move left
        while (loopCounterX >= 0) :
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterX -= 1
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)

        # move up
        while (loopCounterY >= 0) :
            display.set_pixel(loopCounterX, loopCounterY, 9)
            loopCounterY -= 1
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
