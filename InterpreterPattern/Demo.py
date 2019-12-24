# -*- coding:utf-8 -*-
# @time   : 2019-12-24 16:39
# @author : xulei
# @project: DesignPattern

from InterpreterPattern.Expression import TerminalExpression, OrExpression, AndExpression


class Demo:
    # 规则：Robert 和 John 是男性
    def getMaleExpression(self):
        robert = TerminalExpression('Robert')
        john = TerminalExpression('John')
        return OrExpression(robert, john)

    # 规则：Julie 是一个已婚的女性
    def getMarriedWomanExpression(self):
        julie = TerminalExpression('Julie')
        married = TerminalExpression('Married')
        return AndExpression(julie, married)


if __name__ == '__main__':
    demo = Demo()
    isMale = demo.getMaleExpression()
    isMarriedWoman = demo.getMarriedWomanExpression()

    print('Join is male?', isMale.interpret('John'))
    print('Julie is a married women?', isMarriedWoman.interpret('Married Julie'))
    '''
    Join is male? True
    Julie is a married women? True
    '''