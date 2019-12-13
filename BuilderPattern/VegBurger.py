# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:27
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Burger import Burger


# Burger的实体类
class VegBurger(Burger):
    def price(self):
        return 25.0

    def name(self):
        return 'Veg Burger'
