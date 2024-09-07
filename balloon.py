import pygame
from pygame import Rect, Surface, Vector2
from math import sqrt


class Balloon:
  def __init__(self):
    self.rect : Rect = Rect(300,100,30,30)
    self.velocity: Vector2 = Vector2(0,0)
    self.count = 0
  
    
  def update(self):
    #gravity
    self.velocity.y += 0.7
    self.rect.y += int(self.velocity.y)
    self.rect.x += int(self.velocity.x)
    #drag
    self.velocity *= 0.80 # coefficent of drag
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    distance: float = sqrt((self.rect.centery-y)**2 + (self.rect.centerx-x)**2)
    if distance <= 10:
      self.velocity.x = (self.rect.centerx - x)*4
      self.velocity.y = (self.rect.centery - y)*4
      self.count += 1
      
      
  def draw(self,screen : Surface):
    pygame.draw.ellipse(screen,(155,0,0), self.rect)