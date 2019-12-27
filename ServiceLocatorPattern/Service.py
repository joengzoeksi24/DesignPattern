# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:49
# @author : xulei
# @project: DesignPattern

import abc


# 创建服务接口 Service
class Service(abc.ABC):
    def getName(self):
        """"""

    def execute(self):
        """"""


# 创建实体服务
class Service1(Service):
    def execute(self):
        print('Executing Service1.')

    def getName(self):
        return 'Service1'


class Service2(Service):
    def execute(self):
        print('Eecuting Service2.')

    def getName(self):
        return 'Service2'

