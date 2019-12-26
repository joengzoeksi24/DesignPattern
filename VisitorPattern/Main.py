# -*- coding:utf-8 -*-
# @time   : 2019-12-26 10:28
# @author : xulei
# @project: DesignPattern

from VisitorPattern.Visitor import ComputerPartDisplayVisitor
from VisitorPattern.ComputerPart import Computer


# 使用 ComputerPartDisplayVisitor 来显示 Computer 的组成部分
if __name__ == '__main__':
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())
    '''
    Displaying Mouse.
    Displaying Keyboard.
    Displaying Monitor.
    Displaying Computer.
    '''