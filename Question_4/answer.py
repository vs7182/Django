class Rectangle:
    # Initializing Rectangle class with length and width attributes
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Making the Rectangle instance iterable
    def __iter__(self):
        # Yielding the length first in the required dictionary format
        yield {'length': self.length}
        # Yielding the width next in the required dictionary format
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)
for dimension in rect:
    print(dimension)
