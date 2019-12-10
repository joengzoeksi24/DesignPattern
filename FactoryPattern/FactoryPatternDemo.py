# -*- coding:utf-8 -*-
# @time   : 2019-12-10 16:10
# @author : xulei
# @project: DesignPattern

from FactoryPattern.ShapeFactory import ShapeFactory


if __name__ == '__main__':
    sf = ShapeFactory()
    shape0 = sf.getShape('')
    shape0.draw()

    shape1 = sf.getShape('rectangle')
    shape1.draw()

    shape2 = sf.getShape('Square')
    shape2.draw()
