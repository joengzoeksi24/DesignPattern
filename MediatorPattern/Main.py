# -*- coding:utf-8 -*-
# @time   : 2019-12-25 10:05
# @author : xulei
# @project: DesignPattern

from MediatorPattern.User import User


if __name__ == '__main__':
    robert = User('Robert')
    john = User('John')

    robert.sendMessage('hi, John!')
    john.sendMessage('Hello! Robert!')

'''
2019-12-25 10:44:26.343242  [Robert]: hi, John!
2019-12-25 10:44:26.343263  [John]: Hello! Robert!
'''