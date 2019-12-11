# -*- coding:utf-8 -*-
# @time   : 2019-12-11 14:47
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.color import Color


class Red(Color):
    def fill(self):
        print('Red:fill() method.')
