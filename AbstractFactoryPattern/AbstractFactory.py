# -*- coding:utf-8 -*-
# @time   : 2019-12-11 14:51
# @author : xulei
# @project: DesignPattern

import abc

#为Color和Shape对象创建抽象类来获取工厂
class AbstractFactory(abc.ABC):
    def getColor(self, color:str):
        ''''''

    def getShape(self, shape:str):
        ''''''
