# -*- coding:utf-8 -*-
# @time   : 2019-12-23 10:26
# @author : xulei
# @project: DesignPattern

from DecoratorPattern.interface import Shape


# 创建实现接口的实体类
class Rectangle(Shape):
    def draw(self):
        print('Shape: Rectangle')


class Circle(Shape):
    def draw(self):
        print('Shape: Circle')


