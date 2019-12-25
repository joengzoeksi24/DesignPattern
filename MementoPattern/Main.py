# -*- coding:utf-8 -*-
# @time   : 2019-12-25 10:52
# @author : xulei
# @project: DesignPattern

from MementoPattern.Class import CareTaker, Originator


# 使用 CareTaker 和 Originator 对象
if __name__ == '__main__':
    originator = Originator()
    careTaker = CareTaker()
    originator.setState('State #1')
    originator.setState('State #2')
    careTaker.add(originator.saveStateMemento())
    originator.setState('State #3')
    careTaker.add(originator.saveStateMemento())
    originator.setState('State #4')

    print('Current State: ', originator.getState())
    originator.getStateFromMemento(careTaker.get(0))
    print('First saved Stated: ', originator.getState())
    originator.getStateFromMemento(careTaker.get(1))
    print('Second saved State: ', originator.getState())
'''
Current State:  State #4
First saved Stated:  State #2
Second saved State:  State #3
'''
