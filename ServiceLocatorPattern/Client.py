# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:51
# @author : xulei
# @project: DesignPattern

from ServiceLocatorPattern.ServiceLocator import ServiceLocator


# 使用 ServiceLocator 来演示服务定位器设计模式
if __name__ == '__main__':
    service = ServiceLocator().getService('Service1')
    service.execute()
    service = ServiceLocator().getService('Service2')
    service.execute()
    ServiceLocator().getService('Service1').execute()
    ServiceLocator().getService('Service3').execute()
'''
Executing Service1.
Looking up and creating a new Service2 object.
Eecuting Service2.
Returning cached Service1 object.
Executing Service1.
AttributeError: 'NoneType' object has no attribute 'execute'
'''
