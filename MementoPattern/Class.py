# -*- coding:utf-8 -*-
# @time   : 2019-12-25 10:52
# @author : xulei
# @project: DesignPattern


# 创建 Memento 类:包含了要被恢复的对象的状态
class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state


# 创建 Originator 类:创建并在 Memento 对象中存储状态
class Originator:
    state = ''
    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def saveStateMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()


# 创建 CareTaker 类:负责从 Memento 中恢复对象的状态
class CareTaker:
    mementoList = []

    def add(self, state):
        self.mementoList.append(state)

    def get(self, index):
        return self.mementoList[index]

