class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, speed):
        self.x += speed
        self.y += speed