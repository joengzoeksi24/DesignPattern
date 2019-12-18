# -*- coding:utf-8 -*-
# @time   : 2019-12-18 10:41
# @author : xulei
# @project: DesignPattern

import abc


# 创建桥接实现接口
class DrawAPI(abc.ABC):
    @abc.abstractmethod
    def drawCircle(self, radius, x, y):
        """"""


# 使用 DrawAPI 接口创建抽象类 Shape
class Shape(abc.ABC):

    def __init__(self, drawAPI):
        self._drawAPI = drawAPI

    @abc.abstractmethod
    def draw(self):
        """"""
