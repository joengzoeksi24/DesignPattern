# -*- coding:utf-8 -*-
# @time   : 2019-12-11 15:09
# @author : xulei
# @project: DesignPattern

from AbstractFactoryPattern.FactoryProducer import FactoryProducer


#使用FactoryProducer来获取AbstractFactory，通过传递类型信息来获取实体类的对象
if __name__ == '__main__':

    #获取形状工厂
    shapeFactory = FactoryProducer('Shape').getFactory()
    #获取形状为Rectangle的对象
    shape1 = shapeFactory.getShape('Rectangle')
    shape1.draw() #Rectangle:draw() method.

    #获取颜色工厂
    colorFactory = FactoryProducer('Color').getFactory()
    #获取颜色为Red的对象
    color1 = colorFactory.getColor('Red')
    color1.fill() #Red:fill() method.

