# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:50
# @author : xulei
# @project: DesignPattern


# 创建缓存 Cache
class Cache:
    def __init__(self):
        self.services = []

    def getService(self, serviceName):
        for service in self.services:
            if service.getName().lower() == serviceName.lower():
                print('Returning cached {} object.'.format(serviceName))
                return service
        return None

    def addService(self, newService):
        if newService not in self.services:
            self.services.append(newService)