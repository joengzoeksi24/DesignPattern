# -*- coding:utf-8 -*-
# @time   : 2019-12-24 16:39
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个表达式接口
class Expression(abc.ABC):
    @abc.abstractmethod
    def interpret(self, context):
        """"""


# 创建实现了上述接口的实体类
class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        if self.data in context:
            return True
        return False


class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

