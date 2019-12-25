# -*- coding:utf-8 -*-
# @time   : 2019-12-25 09:22
# @author : xulei
# @project: DesignPattern

import abc


# 创建接口
class Iterator(abc.ABC):
    @abc.abstractmethod
    def hasNext(self):
        """"""

    @abc.abstractmethod
    def next(self):
        """"""


class Container(abc.ABC):
    @abc.abstractmethod
    def getIterator(self):
        """"""
