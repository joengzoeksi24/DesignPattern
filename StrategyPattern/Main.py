# -*- coding:utf-8 -*-
# @time   : 2019-12-26 08:56
# @author : xulei
# @project: DesignPattern

from StrategyPattern.Context import Context
from StrategyPattern.Strategy import OperationAdd, OperationMultiply, OperationSubstract


if __name__ == '__main__':
    context = Context()

    context.setStrategy(OperationAdd())
    print('10 + 5 = ', context.executeStrategy(10, 5))
    context.setStrategy(OperationSubstract())
    print('10 - 5 = ', context.executeStrategy(10, 5))
    context.setStrategy(OperationMultiply())
    print('10 * 5 = ', context.executeStrategy(10, 5))
    '''
    10 + 5 =  15
    10 - 5 =  5
    10 * 5 =  50
    '''