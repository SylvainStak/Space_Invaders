class Player:

    def __init__(self, x, y, sprite, speed):
        self.X = x
        self.Y = y
        self.Sprite = sprite
        self.Speed = speed

    def moveLeft(self):
        if self.X >= 5:
            self.X -= self.Speed

    def moveRight(self):
        if self.X <= 763:
            self.X += self.Speed
