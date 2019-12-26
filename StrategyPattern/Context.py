# -*- coding:utf-8 -*-
# @time   : 2019-12-26 08:56
# @author : xulei
# @project: DesignPattern

from StrategyPattern.Strategy import Strategy


class Context:
    def executeStrategy(self, num1, num2):
        return self.strategy.doOperation(num1, num2)

    def setStrategy(self, strategy):
        self.strategy = strategy