import pygame as pygame
import time
import sys
import os

background_colour = (100,200,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
color = (20, 19, 240)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
boat = pygame.image.load('sailboatcu.jpeg').convert()
boat = pygame.transform.scale(boat, (40, 50))
x = 0
y = 0
vel = 10
pygame.display.flip()
running = True
while running:
  pygame.time.delay(10)

  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
  for event in pygame.event.get():

    # if event object type is QUIT
    # then quitting the pygame
    # and program both.
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= vel

  if keys[pygame.K_RIGHT]:
    x += vel

  if keys[pygame.K_UP]:
    y -= vel

  if keys[pygame.K_DOWN]:
    y += vel
  screen.fill(background_colour)
  screen.blit(boat, (x, y))
  pygame.display.update()

  if event.type == pygame.QUIT:
    running = False

pygame.quit()


