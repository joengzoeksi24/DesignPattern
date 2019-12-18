# -*- coding:utf-8 -*-
# @time   : 2019-12-18 10:41
# @author : xulei
# @project: DesignPattern

from BridgePattern.interface import DrawAPI
from BridgePattern.interface import Shape


# 创建实现了 DrawAPI 接口的实体桥接实现类
class RedCircle(DrawAPI):
    def drawCircle(self, radius, x, y):
        print('Drawing Circle[color:red, radius: {}, x: {}, y: {}]'.format(radius, x, y))


class GreenCircle(DrawAPI):
    def drawCircle(self, radius, x, y):
        print('Drawing Circle[color:green, radius: {}, x: {}, y: {}]'.format(radius, x, y))


# 创建实现了 Shape 接口的实体类
class Circle(Shape):

    def __init__(self, x, y, radius, drawAPI:DrawAPI):
        super().__init__(drawAPI)
        self.__x = x
        self.__y = y
        self.__radius = radius

    def draw(self):
        self._drawAPI.drawCircle(self.__radius, self.__x, self.__y)


