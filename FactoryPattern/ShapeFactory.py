# -*- coding:utf-8 -*-
# @time   : 2019-12-10 16:03
# @author : xulei
# @project: DesignPattern

from FactoryPattern.shape import Shape
from FactoryPattern.Rectangle import Rectangle
from FactoryPattern.Square import Square


#创建一个工厂，生成基于给定信息的实体类的对象
class ShapeFactory:
    def getShape(self, shapeType:str):
        if shapeType == 'rectangle':
            return Rectangle()
        if shapeType == 'Square':
            return Square()


        return Shape()
