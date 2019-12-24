# -*- coding:utf-8 -*-
# @time   : 2019-12-24 15:25
# @author : xulei
# @project: DesignPattern

import abc
from CommandPattern.Stock import Stock


# 创建一个命令接口
class Order(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        """"""


# 创建实现了 Order 接口的实体类
class BuyStock(Order):
    def __init__(self, abcStock: Stock):
        self.abcStock = abcStock

    def execute(self):
        self.abcStock.buy()


class SellStock(Order):
    def __init__(self, abcStock:Stock):
        self.abcStock = abcStock

    def execute(self):
        self.abcStock.sell()


