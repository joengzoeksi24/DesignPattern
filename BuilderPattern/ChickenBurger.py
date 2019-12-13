# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:29
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Burger import Burger


# Burger的实体类
class ChickenBurger(Burger):
    def price(self):
        return 50.5

    def name(self):
        return 'Chicken Burger'

