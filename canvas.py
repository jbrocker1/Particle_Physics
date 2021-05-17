class Canvas:
  def __init__(self, *args, color: tuple[int, int, int] = (100, 100, 100)) -> None:
    if len(args) == 0:
      self.width = 500
      self.height = 500
    elif type(args[0]) == tuple:
      self.width: int = args[0][0]
      self.height: int = args[0][1]
    elif type(args[0]) == int and type(args[1]) == int:
      self.width: int = args[0]
      self.height: int = args[1]
    else:
      raise TypeError("Must enter two ints or a tuple of two ints")

    self.color = color

  def point(self) -> tuple[int, int]:
    return self.width, self.height

  def half(self) -> "Canvas":
    return Canvas(self.width // 2, self.height // 2)

  def __str__(self):
    return "({}, {})".format(self.width, self.height)
