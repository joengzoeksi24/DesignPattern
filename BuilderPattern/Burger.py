# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:22
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Item import Item
from BuilderPattern.Wrapper import Wrapper

# 实现Item接口的抽象类，该类提供了默认的功能
class Burger(Item):
    def packing(self):
        return Wrapper()
    def price(self):
        """"""
