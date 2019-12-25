# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:17
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个状态接口
class State(abc.ABC):
    @abc.abstractmethod
    def doAction(self, context):
        """"""


# 创建实现接口的实体类
class StartState(State):
    def doAction(self, context):
        print('Player is in start state')
        context.setState(self)

    def toString(self):
        return 'Start State'


class StopState(State):
    def doAction(self, context):
        print('Player is in stop state')
        context.setState(self)

    def toString(self):
        return 'Stop State'

