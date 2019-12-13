# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:24
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Item import Item
from BuilderPattern.Bottle import Bottle


# 实现Item接口的抽象类，该类提供了默认的功能
class ColdDrink(Item):
    def packing(self):
        return Bottle()

    def price(self):
        """"""
