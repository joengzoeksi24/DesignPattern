# -*- coding:utf-8 -*-
# @time   : 2019-12-10 15:48
# @author : xulei
# @project: DesignPattern

from FactoryPattern.shape import Shape

#实现接口的实体类
class Rectangle(Shape):
    def draw(self):
        print("Rectangle:draw() method.")

