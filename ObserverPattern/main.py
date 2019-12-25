# -*- coding:utf-8 -*-
# @time   : 2019-12-25 11:15
# @author : xulei
# @project: DesignPattern

from ObserverPattern.Subject import Subject
from ObserverPattern.Observer import BinaryObserver, OctalObserver, HexaObserver


# 使用 Subject 和实体观察者对象
if __name__ == '__main__':
    subject = Subject()
    HexaObserver(subject)
    OctalObserver(subject)
    BinaryObserver(subject)

    print('First state change: 15')
    subject.setState(15)
    print('Second state change: 10')
    subject.setState(10)
'''
First state change: 15
Hex String:  15
Octal String:  15
Binary String:  15
Second state change: 10
Hex String:  10
Octal String:  10
Binary String:  10
'''