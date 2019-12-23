# -*- coding:utf-8 -*-
# @time   : 2019-12-23 15:24
# @author : xulei
# @project: DesignPattern

from ChainOfResponsibilityPattern.Abstract import AbstractLogger


# 创建扩展了该记录器类的实体类
class ConsoleLogger(AbstractLogger):
    def __init__(self, level):
        super().__init__(level)
        # self.level = level

    def write(self, message):
        print('Standard Console::Logger: ', message)


class ErrorLogger(AbstractLogger):
    def __init__(self, level):
        super().__init__(level)
        # self.level = level

    def write(self, message):
        print('Error Console::Looger: ',message)


class FileLogger(AbstractLogger):
    def __init__(self, level):
        super().__init__(level)
        # self.level = level

    def write(self, message):
        print('File::Logger: ', message)

