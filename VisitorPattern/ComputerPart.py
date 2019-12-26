# -*- coding:utf-8 -*-
# @time   : 2019-12-26 10:28
# @author : xulei
# @project: DesignPattern

import abc
# from VisitorPattern.Visitor import ComputerPartVisitor


# 定义一个表示元素的接口
class ComputerPart(abc.ABC):
    def accept(self, visitor):
        """"""


# 创建扩展了上述类的实体类
class Keyboard(ComputerPart):
    def accept(self, visitor):
        visitor.visitKeyboard(self)


class Monitor(ComputerPart):
    def accept(self, visitor):
        visitor.visitMonitor(self)


class Mouse(ComputerPart):
    def accept(self, visitor):
        visitor.visitMouse(self)


class Computer(ComputerPart):
    parts = []

    def __init__(self):
        self.parts = [Mouse(), Keyboard(), Monitor()]

    def accept(self, visitor):
        for i in range(len(self.parts)):
            self.parts[i].accept(visitor)
        visitor.visitComputer(self)

