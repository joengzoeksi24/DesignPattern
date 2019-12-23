# -*- coding:utf-8 -*-
# @time   : 2019-12-23 15:24
# @author : xulei
# @project: DesignPattern

from ChainOfResponsibilityPattern.Abstract import AbstractLogger
from ChainOfResponsibilityPattern.Class import ConsoleLogger, ErrorLogger, FileLogger


# 创建不同类型的记录器。赋予它们不同的错误级别，并在每个记录器中设置下一个记录器。每个记录器中的下一个记录器代表的是链的一部分
class ChainPatternDemo:
    def getChainOfLoggers(self):
        errorLogger = ErrorLogger(AbstractLogger.ERROR)
        fileLogger = FileLogger(AbstractLogger.DEBUG)
        consoleLogger = ConsoleLogger(AbstractLogger.INFO)

        errorLogger.setNextLogger(fileLogger)
        fileLogger.setNextLogger(consoleLogger)

        return errorLogger


if __name__ == '__main__':
    loggerChain = ChainPatternDemo().getChainOfLoggers()

    loggerChain.logMessage(AbstractLogger.INFO, 'This is an information.')
    print()
    loggerChain.logMessage(AbstractLogger.DEBUG, 'This is a debug level ingormation.')
    print()
    loggerChain.logMessage(AbstractLogger.ERROR, 'This is an error information.')

    '''
    Standard Console::Logger:  This is an information.

    File::Logger:  This is a debug level ingormation.
    Standard Console::Logger:  This is a debug level ingormation.
    
    Error Console::Looger:  This is an error information.
    File::Logger:  This is an error information.
    Standard Console::Logger:  This is an error information.
    '''