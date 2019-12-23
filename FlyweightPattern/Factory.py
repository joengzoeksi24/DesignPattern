# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:55
# @author : xulei
# @project: DesignPattern

from collections import defaultdict
from FlyweightPattern.Class import Circle


# 创建一个工厂，生成基于给定信息的实体类的对象
class ShapeFactory:
    circleMap = defaultdict(None)

    def getCircle(self, color):
        self.circleMap.setdefault(color, None)
        circle = self.circleMap[color]
        if circle is None:
            circle = Circle(color)
            self.circleMap[color] = circle
            print('Creating circle of color: ', color)

        return circle
