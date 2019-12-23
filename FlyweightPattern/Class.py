# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:55
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个接口
class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        """"""


# 创建实现接口的实体类
class Circle(Shape):
    def __init__(self, color):
        self.color = color
        self.x = None
        self.y = None
        self.radius = None

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setRadius(self, radius):
        self.radius = radius

    def draw(self):
        print('Circle: Draw() [Color: {}, x: {}, y: {}, radius: {}'.format(self.color, self.x, self.y, self.radius))

