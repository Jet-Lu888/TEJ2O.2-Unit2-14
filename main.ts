/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Jet Lu
 * Created on: Apr 2026
 * This program makes a sprite go around the screen.
*/

// setup
basic.showIcon(IconNames.Happy)

// variables
let loopCounterX = 0
let loopCounterY = 0
let sprite: game.LedSprite = null

// button a
input.onButtonPressed(Button.A,  function () {
  // setup
  basic.clearScreen()
  loopCounterX = 0
  loopCounterY = 0
  sprite = game.createSprite(0, 0)

  // move
  while (loopCounterX <= 4) {
    sprite.set(LedSpriteProperty.X, loopCounterX)
    loopCounterX += 1
    basic.pause(500)
  }
  while (loopCounterY <= 4) {
    sprite.set(LedSpriteProperty.Y, loopCounterY)
    loopCounterY += 1
    basic.pause(500)
  }
  while (loopCounterX >= 0) {
    sprite.set(LedSpriteProperty.X, loopCounterX)
    loopCounterX -= 1
    basic.pause(500)
    }
  while (loopCounterY >= 0) {
    sprite.set(LedSpriteProperty.Y, loopCounterY)
    loopCounterY -= 1
    basic.pause(500)
  }
  sprite.delete()
  basic.pause(500)
  basic.showIcon(IconNames.Happy)
})

// button b
input.onButtonPressed(Button.B, function () {
  // setup
  basic.clearScreen()
  loopCounterX = 0
  loopCounterY = 0
  sprite = game.createSprite(0, 0)

  // move
  while (loopCounterY <= 4) {
    sprite.set(LedSpriteProperty.Y, loopCounterY)
    loopCounterY += 1
    basic.pause(500)
  }
  while (loopCounterX <= 4) {
    sprite.set(LedSpriteProperty.X, loopCounterX)
    loopCounterX += 1
    basic.pause(500)
  }
  while (loopCounterY >= 0) {
    sprite.set(LedSpriteProperty.Y, loopCounterY)
    loopCounterY -= 1
    basic.pause(500)
  }
  while (loopCounterX >= 0) {
    sprite.set(LedSpriteProperty.X, loopCounterX)
    loopCounterX -= 1
    basic.pause(500)
  }
  sprite.delete()
  basic.pause(500)
  basic.showIcon(IconNames.Happy)
})
