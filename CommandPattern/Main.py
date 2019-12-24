# -*- coding:utf-8 -*-
# @time   : 2019-12-24 15:25
# @author : xulei
# @project: DesignPattern

from CommandPattern.Stock import Stock
from CommandPattern.Order import BuyStock, SellStock
from CommandPattern.Broker import Broker


if __name__ == '__main__':
    abcStock = Stock()
    buyStockOrder = BuyStock(abcStock)
    sellStockOrder = SellStock(abcStock)
    broker = Broker()
    print(broker.__dir__())
    print(broker.__dict__)
    broker.takeOrder(buyStockOrder)
    broker.takeOrder(sellStockOrder)
    broker.placeOrders()
    '''
    ['__module__', 'orderList', 'takeOrder', 'placeOrders', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
    {}
    Stock [Name: ABC, Quantity: 10] bought
    Stock [Name: ABC, Quantity: 10] sold
    '''

