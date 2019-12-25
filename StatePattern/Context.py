# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:18
# @author : xulei
# @project: DesignPattern

from StatePattern.State import State


# 一个带有某个状态的类
class Context:
    state: State = None

    def __init__(self):
        self.state = None

    def setState(self, state: State):
        self.state = state

    def getState(self):
        return self.state