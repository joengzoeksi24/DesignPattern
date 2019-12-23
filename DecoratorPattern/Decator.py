# -*- coding:utf-8 -*-
# @time   : 2019-12-23 10:25
# @author : xulei
# @project: DesignPattern

from DecoratorPattern.interface import Shape


# 创建实现了 Shape 接口的抽象装饰类
class ShapeDecorator(Shape):
    def __init__(self, decoratedShape):
        super().__init__()
        self.decoratedShape = decoratedShape
        print('ShapeDecorator __init__')

    def draw(self):
        self.decoratedShape.draw()


# 创建扩展了 ShapeDecorator 类的实体装饰类
class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decoratedShape):
        super().__init__(decoratedShape)
        self.decoratedShape = decoratedShape
        self.des.append('RedShapeDecorator')
        print('RedShapeDecorator __init__')

    def draw(self):
        self.decoratedShape.draw()
        self.setRedBorder()

    def setRedBorder(self):
        print('Border Color: Red')


class BlackTextDecorator(ShapeDecorator):
    def __init__(self, decoratedShape):
        super().__init__(decoratedShape)
        self.decoratedShape = decoratedShape
        self.des.append('BlackTextDecorator')
        print('BlackTextDecorator __init__')

    def draw(self):
        self.decoratedShape.draw()
        self.write()

    def write(self):
        print('Text Color: black')