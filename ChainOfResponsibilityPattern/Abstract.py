# -*- coding:utf-8 -*-
# @time   : 2019-12-23 15:24
# @author : xulei
# @project: DesignPattern

import abc


# 创建抽象的记录器类
class AbstractLogger(abc.ABC):
    INFO, DEBUG, ERROR = 1, 2, 3
    # _level = None
    _nextLogger = None

    def __init__(self, level):
        self._level = level

    def setNextLogger(self, nextLogger):
        self._nextLogger = nextLogger

    @abc.abstractmethod
    def write(self, message):
        """"""

    def logMessage(self, level, message):
        if self._level <= level:
            self.write(message)
        if self._nextLogger is not None:
            self._nextLogger.logMessage(level, message)
