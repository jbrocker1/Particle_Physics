import pygame
import random
from sys import exit
from canvas import Canvas
from vector import Vector

class Particle:
  def __init__(self, position: Vector = Vector(), velocity: Vector = Vector()) -> None:
    self.pos: Vector = position
    self.vel: Vector = velocity



def main() -> None:
  canvas = Canvas()
  win = pygame.display.set_mode(canvas.point())





  while True:
    win.fill(canvas.color)

    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()


if __name__ == "__main__":
  main()
