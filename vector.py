import globals

class Vector:
  def __init__(self, x: float = 0, y: float = 0) -> None:
    self.x: float = x
    self.y: float = y

  def point(self) -> tuple[float, float]:
    return self.x, self.y

  def __add__(self, other: "Vector") -> "Vector":
    return Vector(self.x + other.x, self.y + other.y)

  def __sub__(self, other: "Vector") -> "Vector":
    return Vector(self.x - other.x, self.y - other.y)

  def __mul__(self, other: "Vector") -> "Vector":
    return Vector(self.x * other.x, self.y * other.y)

  def __str__(self):
    return "({}, {})".format(self.x, self.y)
