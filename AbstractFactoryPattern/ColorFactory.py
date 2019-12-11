# -*- coding:utf-8 -*-
# @time   : 2019-12-11 14:54
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.AbstractFactory import AbstractFactory
from AbstractFactoryPattern.Red import Red
from AbstractFactoryPattern.Blue import Blue


#创建扩展了AbstractFactory的工厂类，基于给定的信息生成实体类的信息
class ColorFactory(AbstractFactory):
    def getColor(self, color:str):
        if color == '':
            return None
        if color == 'Red':
            return Red()
        if color == 'Blue':
            return Blue()

        return None

    def getShape(self, shape:str):
        return None
