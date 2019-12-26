# -*- coding:utf-8 -*-
# @time   : 2019-12-26 08:56
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个接口
class Strategy(abc.ABC):
    def doOperation(self, num1, num2):
        """"""


# 创建实现接口的实体类
class OperationAdd(Strategy):
    def doOperation(self, num1, num2):
        return num1 + num2


class OperationSubstract(Strategy):
    def doOperation(self, num1, num2):
        return num1 - num2


class OperationMultiply(Strategy):
    def doOperation(self, num1, num2):
        return num1 * num2


