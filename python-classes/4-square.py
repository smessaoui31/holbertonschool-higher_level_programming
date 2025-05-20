#!usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size  # Use the setter

    @property
    def size(self):
        return self.__size  # Getter

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
    