class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def left(self):
        self.x -= 1
    
    def right(self):
        self.x += 1
    
    def up(self):
        self.y -= 1
    
    def down(self):
        self.y += 1
    
    def position(self):
        return (self.x, self.y)
