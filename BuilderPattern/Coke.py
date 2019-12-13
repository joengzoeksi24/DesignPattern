# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:30
# @author : xulei
# @project: DesignPattern

from BuilderPattern.ColdDrink import ColdDrink


# ColdDrink实体类
class Coke(ColdDrink):
    def price(self):
        return 30.0

    def name(self):
        return 'Coke'
