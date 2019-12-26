# -*- coding:utf-8 -*-
# @time   : 2019-12-26 10:28
# @author : xulei
# @project: DesignPattern

import abc
from VisitorPattern.ComputerPart import Computer, Monitor, Mouse, Keyboard


# 定义一个表示访问者的接口
class ComputerPartVisitor(abc.ABC):
    def visitComputer(self, computer: Computer):
        """"""

    def visitMouse(self, mouse: Mouse):
        """"""

    def visitKeyboard(self, keyboard: Keyboard):
        """"""

    def visitMonitor(self, monitor: Monitor):
        """"""


# 创建实现了上述类的实体访问者
class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visitComputer(self, computer: Computer):
        print('Displaying Computer.')

    def visitMouse(self, mouse: Mouse):
        print('Displaying Mouse.')

    def visitKeyboard(self, keyboard: Keyboard):
        print('Displaying Keyboard.')

    def visitMonitor(self, monitor: Monitor):
        print('Displaying Monitor.')

