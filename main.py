from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.time import Clock
from pygame import surface
from pygame.locals import *
from sys import exit
from balloon import Balloon

# settings
pygame.init()
FPS: int = 50
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("template")
clock: Clock = Clock()
balloon: Balloon = Balloon()


# game loop
def main():
  while True:
    handle_events()
    update()
    draw()


# event handling
def handle_events():
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    


def update():
  clock.tick(FPS)
  balloon.update()


# drawing
def draw():
  screen.fill((100, 100, 100))
  # font settings
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render("Juggles " + str(balloon.count), True, (0, 0, 0), (100, 100, 100))
  textRect = text.get_rect()
  textRect.x, textRect.y = 0, 0
  screen.blit(text, textRect)
  balloon.draw(screen)
  pygame.display.flip()

main()
