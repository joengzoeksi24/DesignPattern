# -*- coding:utf-8 -*-
# @time   : 2019-12-25 09:23
# @author : xulei
# @project: DesignPattern

from IteratorPattern.Class import NameRepository


if __name__ == '__main__':
    namesRepository = NameRepository()
    iter = namesRepository.getIterator()
    while iter.hasNext():
        print('Name: ', iter.next())
'''
Name:  Robert
Name:  John
Name:  Julie
Name:  Lora
'''