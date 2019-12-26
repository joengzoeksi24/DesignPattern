# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:47
# @author : xulei
# @project: DesignPattern

from CompositeEntityPattern.Client import Client


if __name__ == '__main__':
    client = Client()
    client.setData('Test', 'Data')
    client.printData()
    client.setData('Second Test', 'Data1')
    client.printData()
    '''
    Data:  Test
    Data:  Data
    Data:  Second Test
    Data:  Data1
    '''