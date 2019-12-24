# -*- coding:utf-8 -*-
# @time   : 2019-12-24 15:25
# @author : xulei
# @project: DesignPattern

from CommandPattern.Order import Order


# 创建命令调用类
class Broker:
    orderList = []

    def takeOrder(self, order:Order):
        self.orderList.append(order)

    def placeOrders(self):
        for ordr in self.orderList:
            ordr.execute()
        self.orderList.clear()
