# -*- coding:utf-8 -*-
# @time   : 2019-12-25 11:15
# @author : xulei
# @project: DesignPattern


# 创建 Subject 类
class Subject:
    __observers = []
    __state = ''

    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state
        self.notifyAllObservers()

    def attach(self, observer):
        self.__observers.append(observer)

    def notifyAllObservers(self):
        for observer in self.__observers:
            observer.update()