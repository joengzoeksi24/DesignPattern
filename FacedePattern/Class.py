# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:26
# @author : xulei
# @project: DesignPattern

import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        """"""


# 创建实现接口的实体类
class Circle(Shape):
    def draw(self):
        print('Circle: draw()')


class Rectagnle(Shape):
    def draw(self):
        print('Rectangle: draw()')
