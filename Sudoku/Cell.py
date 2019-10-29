class Cell:
    def __init__(self, value=1, prepopulated=False):
        self.value = value
        self.prepopulated = prepopulated

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def populate_value(self, value):
        self.prepopulated = True
        self.value = int(value)

    def set_value(self, value):
        if not self.prepopulated:
            self.value = int(value)
