# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:50
# @author : xulei
# @project: DesignPattern

from ServiceLocatorPattern.Service import Service1, Service2


# 为 JNDI 查询创建 InitialContext
class InitialContext:
    def lookup(self, jndiName):
        if jndiName.lower() == 'service1':
            print('Looking up and creating a new Service1 object.')
            return Service1()
        elif jndiName.lower() == 'service2':
            print('Looking up and creating a new Service2 object.')
            return Service2()

        return None

