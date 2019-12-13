# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:13
# @author : xulei
# @project: DesignPattern

import abc
from BuilderPattern.Packing import Packing


# 表示食物条目的接口
class Item(abc.ABC):
    def name(self) -> str:
        """"""
    def packing(self) -> Packing:
        """"""
    def price(self) -> float:
        """"""
