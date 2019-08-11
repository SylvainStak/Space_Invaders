class Bullet:

    def __init__(self, x, y, sprite, speed):
        self.X = x
        self.Y = y
        self.Sprite = sprite
        self.Speed = speed

    def move(self):
        self.Y -= self.Speed