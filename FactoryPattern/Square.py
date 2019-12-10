# -*- coding:utf-8 -*-
# @time   : 2019-12-10 16:20
# @author : xulei
# @project: DesignPattern

from FactoryPattern.shape import Shape


#实现接口的实体类
class Square(Shape):
    def draw(self):
        print("Square:draw() method.")