class Invader:

    def __init__(self, x, y, sprite1, sprite2, speed):
        self.X = x
        self.Y = y
        self.actual_sprite = sprite1
        self.Sprite1 = sprite1
        self.Sprite2 = sprite2        
        self.Speed = speed
    
    def move(self, MoveRefX):
        if MoveRefX < 200 or MoveRefX > 600:
            self.Y += 40
            self.Speed = -self.Speed

        self.X += self.Speed

    def changeSprite(self):
        if self.actual_sprite == self.Sprite1:
            self.actual_sprite = self.Sprite2
        else:
            self.actual_sprite = self.Sprite1

        



        

    
