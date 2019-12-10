# -*- coding:utf-8 -*-
# @time   : 2019-12-10 15:26
# @author : xulei
# @project: DesignPattern

import abc


#创建接口类
class Shape(abc.ABC):
    # @abc.abstractmethod #加上这个装饰符，就不能在ShapeFactory类中实例化Shape类了
    def draw(self):
        """抽象方法"""
        print('抽象基类Shape的draw() method.')

    def com(self):
        print("抽象基类Shape的具体方法com")


