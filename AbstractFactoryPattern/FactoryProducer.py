# -*- coding:utf-8 -*-
# @time   : 2019-12-11 15:03
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.ShapeFactory import ShapeFactory
from AbstractFactoryPattern.ColorFactory import ColorFactory


#创建一个工厂创造器/生成器类，通过传递形状或颜色信息来获得工厂
class FactoryProducer:
    def __init__(self, choice):
        self.choice = choice

    def getFactory(self):
        if self.choice == 'Shape':
            return ShapeFactory()
        if self.choice == 'Color':
            return ColorFactory()

        return None

