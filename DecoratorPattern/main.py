# -*- coding:utf-8 -*-
# @time   : 2019-12-23 10:26
# @author : xulei
# @project: DesignPattern

from DecoratorPattern.EntityClass import Circle, Rectangle
from DecoratorPattern.Decator import RedShapeDecorator, BlackTextDecorator


if __name__ == '__main__':
    circle = Circle()
    redCircle = RedShapeDecorator(circle)
    redRectangle = RedShapeDecorator(Rectangle())
    circle.draw()
    print()
    redCircle.draw()
    print()
    redRectangle.draw()
    print()
    '''
    Shape __init__
Shape __init__
ShapeDecorator __init__
RedShapeDecorator __init__
Shape __init__
Shape __init__
ShapeDecorator __init__
RedShapeDecorator __init__
Shape: Circle

Shape: Circle
Border Color: Red

Shape: Rectangle
Border Color: Red
    '''
    blackWrite = BlackTextDecorator(circle)
    blackWrite.draw()
    '''
    Shape __init__
ShapeDecorator __init__
BlackTextDecorator __init__
Shape: Circle
Text Color: black
    '''
    print()
    print(circle.des)
    print(redCircle.des)
    print(blackWrite.des)
    print()
    '''
    ['Shape']
    ['Shape', 'RedShapeDecorator']
    ['Shape', 'BlackTextDecorator']
    '''
    cc = Circle()
    cc = RedShapeDecorator(cc)
    cc = BlackTextDecorator(cc)
    print(cc.draw())
    print()
    print(cc.des)
    '''
    Shape __init__
Shape __init__
ShapeDecorator __init__
RedShapeDecorator __init__
Shape __init__
ShapeDecorator __init__
BlackTextDecorator __init__
Shape: Circle
Border Color: Red
Text Color: black
None

['Shape', 'BlackTextDecorator']
    '''

