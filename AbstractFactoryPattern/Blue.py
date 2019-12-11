# -*- coding:utf-8 -*-
# @time   : 2019-12-11 14:49
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.color import Color


class Blue(Color):
    def fill(self):
        print('Blue:fill() method.')
