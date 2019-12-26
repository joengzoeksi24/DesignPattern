# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:25
# @author : xulei
# @project: DesignPattern

from BusinessDelegatePattern.Serviece import EJBService, JMSService


# 创建业务查询服务
class BusinessLookUp:
    def getBusinessService(self, serviceType):
        if serviceType == 'EJB':
            return EJBService()
        return JMSService()

