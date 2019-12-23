# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:26
# @author : xulei
# @project: DesignPattern

from FacedePattern.Class import Circle, Rectagnle


# 创建一个外观类
class ShapeMaker:
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectagnle()

    def drawCicle(self):
        self.circle.draw()

    def drawRectangle(self):
        self.rectangle.draw()

