import globals
import pygame
from vector import Vector
from canvas import Canvas


class Particle:
  def __init__(self, position: Vector = Vector(), velocity: Vector = Vector(),
               color: tuple[int, int, int] = (255, 255, 255), radius: float = 3,
               gravity: bool = True) -> None:
    self.pos: Vector = position
    self.vel: Vector = velocity
    self.color: tuple[int, int, int] = color
    self.radius: float = radius
    self.gravity: bool = gravity

  def update(self):
    if self.gravity:
      self.vel += globals.gravity
    self.pos += self.vel

  def draw(self, win: pygame.Surface):
    pygame.draw.circle(win, self.color, self.pos.point(), self.radius)


def main() -> None:
  canvas = Canvas()
  win = pygame.display.set_mode(canvas.point())
  clock = pygame.time.Clock()

  p = Particle(Vector(250, 250), Vector(0, -10))

  while True:
    win.fill(canvas.color)
    p.update()
    p.draw(win)

    pygame.display.flip()
    clock.tick(40)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()


if __name__ == "__main__":
  globals.init()
  main()
