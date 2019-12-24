# -*- coding:utf-8 -*-
# @time   : 2019-12-24 15:32
# @author : xulei
# @project: DesignPattern


# 创建一个请求类
class Stock:
    def __init__(self):
        self.name = 'ABC'
        self.quantity = 10

    def buy(self):
        print('Stock [Name: {}, Quantity: {}] bought'.format(self.name, self.quantity))

    def sell(self):
        print('Stock [Name: {}, Quantity: {}] sold'.format(self.name, self.quantity))

