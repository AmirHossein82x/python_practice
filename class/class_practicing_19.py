class Point:
    count = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.count += 1 

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def __add__(self, other): # +

        if isinstance(other, Point):
            new_x = self.__x + other.x
            new_y = self.__y + other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x + other
            new_y = self.__y + other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __sub__(self, other): # -

        if isinstance(other, Point):
            new_x = self.__x - other.x
            new_y = self.__y - other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x - other
            new_y = self.__y - other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __mul__(self, other):  # *

        if isinstance(other, Point):
            new_x = self.__x * other.x
            new_y = self.__y * other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x * other
            new_y = self.__y * other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __floordiv__(self, other): # //

        if isinstance(other, Point):
            new_x = self.__x // other.x
            new_y = self.__y // other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x // other
            new_y = self.__y // other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __truediv__(self, other): #/

        if isinstance(other, Point):
            new_x = self.__x / other.x
            new_y = self.__y / other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x / other
            new_y = self.__y / other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __mod__(self, other):  #%

        if isinstance(other, Point):
            new_x = self.__x % other.x
            new_y = self.__y % other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x % other
            new_y = self.__y % other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __pow__(self, other):

        if isinstance(other, Point):
            new_x = self.__x ** other.x
            new_y = self.__y ** other.y
            return Point(new_x, new_y)
        
        elif isinstance(other, int):
            new_x = self.__x ** other
            new_y = self.__y ** other
            return Point(new_x, new_y)

        else:
            print('invalid input')

    def __lt__(self, other):  # <
        return  self.__x < other.x and self.__y < other.y

    def __le__(self, other):   # <=
        return self.__x <= other.x and self.__y <= other.y

    def __gt__(self, other):   # >
        return  self.__x > other.x and self.__y > other.y
            
    def __ge__(self, other): # >=
        return  self.__x >= other.x and self.__y >= other.y
            
    def __eq__(self, other): # ==
        return self.__x == other.x and self.__y == other.y

    def __ne__(self, other):  # !=
        return self.__x != other.x and self.__y != other.y

    def __getitem__(self, index):
        if index == 0:
            return self.__x
        elif index == 1:
            return self.__y
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        pass

    def __contains__(self, other):
        pass

    def __str__(self):
        return f"({self.__x}, {self.__y})"

a = Point(154, 1)
b = Point(14, 112)