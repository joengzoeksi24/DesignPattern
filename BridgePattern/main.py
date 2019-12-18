# -*- coding:utf-8 -*-
# @time   : 2019-12-18 10:41
# @author : xulei
# @project: DesignPattern

from BridgePattern.EntityClass import Circle, RedCircle, GreenCircle


if __name__ == '__main__':
    redCircle = Circle(100, 100, 10, RedCircle())
    greenCircle = Circle(100, 100, 10, GreenCircle())

    redCircle.draw()
    greenCircle.draw()
'''
Drawing Circle[color:red, radius: 10, x: 100, y: 100]
Drawing Circle[color:green, radius: 10, x: 100, y: 100]
'''
