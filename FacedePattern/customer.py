# -*- coding:utf-8 -*-
# @time   : 2019-12-23 13:26
# @author : xulei
# @project: DesignPattern

from FacedePattern.Maker import ShapeMaker


# 使用该外观类画出各种类型的形状
if __name__ == '__main__':
    shapeMaker = ShapeMaker()
    shapeMaker.drawCicle()
    shapeMaker.drawRectangle()
    '''
    Circle: draw()
    Rectangle: draw()
    '''
