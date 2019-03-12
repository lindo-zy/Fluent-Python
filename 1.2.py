#!/usr/bin/python3
# -*- coding:utf-8 -*-

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    # def __str__(self):
    #     print('hehe')
    #     return 'Vector(%r,%r)' % (self.x, self.y)


if __name__ == '__main__':
    v = Vector(1, 2)
    c = Vector(2, 3)
    # print(v.__repr__())
    # print(v.__abs__())
    # print(v.__bool__())
    # print(v.__add__(c))
    # print(v.__mul__(2))

