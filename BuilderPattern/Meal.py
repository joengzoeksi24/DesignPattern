# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:55
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Item import Item


# 创建一个Meal类，包含Item对象
class Meal:
    items = []

    # def __init__(self):
    #     self.items = []

    def addItem(self,item:Item):
        self.items.append(item)

    def getCost(self):
        cost = 0
        for item in self.items:
            cost += item.price()
        return cost

    def showItems(self):
        for item in self.items:
            print("Item: " + item.name() + ", Packing: " + item.packing().pack() + ", Price: " + str(item.price()))


