# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:50
# @author : xulei
# @project: DesignPattern

from ServiceLocatorPattern.Cache import Cache
from ServiceLocatorPattern.InitialContext import InitialContext


# 创建服务定位器
class ServiceLocator:
    cache = Cache()

    def getService(self, jndiName):
        service = self.cache.getService(jndiName)
        if service is not None:
            return service

        context = InitialContext()
        service1 = context.lookup(jndiName)
        ServiceLocator.cache.addService(service1)
        return service1
