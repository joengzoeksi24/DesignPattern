# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:46
# @author : xulei
# @project: DesignPattern

from BuilderPattern.ColdDrink import ColdDrink


# ColdDrink实体类
class Pepsi(ColdDrink):
    def price(self):
        return 35.0

    def name(self):
        return 'Pepsi'
