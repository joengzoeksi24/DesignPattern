# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:14
# @author : xulei
# @project: DesignPattern

import abc


# 表示食物包装的接口
class Packing(abc.ABC):
    def pack(self) -> str:
        """"""
