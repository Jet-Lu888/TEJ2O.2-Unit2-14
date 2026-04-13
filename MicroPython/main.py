"""
Created by: Jet Lu
Created on: Apr 2026
This module is a Micro:bit MicroPython program that displays a pixel going clockwise and counter clockwise.
"""

from microbit import *

# variables
loopCounterX = 0
loopCounterY = 0

# setup
display.clear()
display.show(Image.HAPPY)
while True:

    # clock wise
    if button_a.was_pressed():

        # setup
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        # goes right
        while loopCounterX < 4:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterX += 1

        # goes down
        while loopCounterY < 4:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterY += 1

        # goes left
        while loopCounterX > 0:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterX -= 1

        # goes up
        while loopCounterY >= 0:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterY -= 1
        display.show(Image.HAPPY)

    # counter clock wise
    if button_b.was_pressed():

        # setup
        display.clear()
        loopCounterX = 0
        loopCounterY = 0

        # goes down
        while loopCounterY < 4:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterY = loopCounterY + 1

        # goes right
        while loopCounterX < 4:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterX = loopCounterX + 1

        # goes up
        while loopCounterY > 0:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterY = loopCounterY - 1

        # goes left
        while loopCounterX >= 0:
            display.set_pixel(loopCounterX, loopCounterY, 9)
            sleep(500)
            display.set_pixel(loopCounterX, loopCounterY, 0)
            loopCounterX = loopCounterX - 1
        display.show(Image.HAPPY)
