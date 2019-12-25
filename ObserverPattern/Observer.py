# -*- coding:utf-8 -*-
# @time   : 2019-12-25 11:15
# @author : xulei
# @project: DesignPattern

import abc
from ObserverPattern.Subject import Subject


# 创建 Observer 类
class Observer(abc.ABC):
    subject = Subject()

    @abc.abstractmethod
    def update(self):
        """"""


# 创建实体观察者类
class BinaryObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('Binary String: ', str(self.subject.getState()))


class OctalObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('Octal String: ', str(self.subject.getState()))


class HexaObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('Hex String: ', str(self.subject.getState()).upper())
