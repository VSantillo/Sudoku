class Pointer:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return self.x, self.y

    def __str__(self):
        return str((self.x, self.y))

    def move(self, n):
        if n == 0:
            # Move up 1
            self.y = min(self.y + 1, 8)
        elif n == 1:
            # Move down 1
            self.y = max(self.y - 1, 0)
        elif n == 2:
            # Move left 1
            self.x = max(self.x - 1, 0)
        elif n == 3:
            # Move right 1
            self.x = min(self.x + 1, 8)