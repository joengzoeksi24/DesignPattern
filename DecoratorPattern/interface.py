# -*- coding:utf-8 -*-
# @time   : 2019-12-23 10:25
# @author : xulei
# @project: DesignPattern

import abc


class Shape(abc.ABC):
    def __init__(self):
        print('Shape __init__')
        self.des = ['Shape']

    @abc.abstractmethod
    def draw(self):
        """"""
