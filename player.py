class player:
    def __init__(self, block, x, y):
            self.x = x
            self.y = y
            self.block = block
    
    def goLeft(self):
        self.x -= 3

    def goRight(self):
        self.x += 3