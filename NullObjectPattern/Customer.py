# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:31
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个抽象类:定义操作（在这里，是客户的名称）的 AbstractCustomer 抽象类
class AbstractCustomer(abc.ABC):
    name = ''

    @abc.abstractmethod
    def isNil(self) -> bool:
        """"""

    @abc.abstractmethod
    def getName(self) -> str:
        """"""


# 创建扩展了上述类的实体类
class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isNil(self):
        return False


class NullCustomer(AbstractCustomer):
    def getName(self):
        return 'Not Available in Customer Database'

    def isNil(self):
        return True


