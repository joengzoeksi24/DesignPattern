# -*- coding:utf-8 -*-
# @time   : 2019-12-23 14:52
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个接口
class Image(abc.ABC):
    @abc.abstractmethod
    def display(self):
        """"""

