import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__z = z

    def get_volume(self):
        return math.pow(self.__radius, 3) * math.pi * 4 / 3

    def get_square(self):
        return 4 * math.pi * math.pow(self.__radius, 2)

    def get_radius(self):
        return self.__radius

    def get_center(self):
        return {self.__x, self.__y, self.__z}

    def set_radius(self, radius):
        self.__radius = radius

    def set_center(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def is_point_inside(self, x, y, z):
        return math.pow(self.__x - x, 2) + math.pow(self.__y - y, 2) + math.pow(self.__z - z, 2) < math.pow(
            self.__radius, 2)
