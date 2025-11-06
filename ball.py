class ball:
    def __init__(self, block, x, y):
        self.x = x
        self.y = y
        self.block = block
    
    def move(self, speed):
        self.x += speed
        self.y += speed