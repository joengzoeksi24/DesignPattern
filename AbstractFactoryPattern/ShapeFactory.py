# -*- coding:utf-8 -*-
# @time   : 2019-12-11 14:54
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactoryPattern.Rectangle import Rectangle
from AbstractFactoryPattern.Square import Square


#创建扩展了AbstractFactory的工厂类，基于给定的信息生成实体类的对象
class ShapeFactory(AbstractFactory):
    def getShape(self, shape:str):
        if shape == "":
            return None
        if shape == 'Rectangle':
            return Rectangle()
        if shape == 'Square':
            return Square()

        return None

    def getColor(self, color:str):
        return None
