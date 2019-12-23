# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:55
# @author : xulei
# @project: DesignPattern

from random import random
from FlyweightPattern.Factory import ShapeFactory


# 使用工厂，通过传递颜色信息来获取实体类的对象
class FlyweightPatternDemo:
    colors = ['Red', 'Green', 'Blue', 'White', 'Black']

    def getRandomColor(self):
        return self.colors[int(random() * len(self.colors))]

    def getRandomX(self):
        return int(random() * 100)

    def getRandomY(self):
        return int(random() * 100)


if __name__ == '__main__':
    fly = FlyweightPatternDemo()

    for i in range(10):
        color = fly.getRandomColor()
        circle = ShapeFactory().getCircle(color)
        circle.setX(fly.getRandomX())
        circle.setY(fly.getRandomY())
        circle.setRadius(100)
        circle.draw()
'''
Creating circle of color:  Red
Circle: Draw() [Color: Red, x: 66, y: 56, radius: 100
Creating circle of color:  Black
Circle: Draw() [Color: Black, x: 28, y: 63, radius: 100
Creating circle of color:  White
Circle: Draw() [Color: White, x: 98, y: 76, radius: 100
Circle: Draw() [Color: Black, x: 8, y: 25, radius: 100
Circle: Draw() [Color: Black, x: 34, y: 93, radius: 100
Circle: Draw() [Color: White, x: 28, y: 71, radius: 100
Creating circle of color:  Blue
Circle: Draw() [Color: Blue, x: 48, y: 45, radius: 100
Circle: Draw() [Color: White, x: 5, y: 79, radius: 100
Creating circle of color:  Green
Circle: Draw() [Color: Green, x: 45, y: 1, radius: 100
Circle: Draw() [Color: Red, x: 88, y: 37, radius: 100
'''
