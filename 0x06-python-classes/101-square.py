#!/usr/bin/python3
"""contains a class that defines a square and its size and its
position on the screen """


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """it Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
            position (tuple): the coordinates of the square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        """it Sets the print behavior of the Square object."""
        square_str = ""

        if self.__size > 0:
            for y in range(self.__position[1]):
                square_str += '\n'
            for x in range(self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'

        return square_str[:-1]

    @property
    def size(self):
        """it Gets or sets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Gets or sets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """it Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """it Prints the square with the # character on stdout"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
