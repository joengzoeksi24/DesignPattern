# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:25
# @author : xulei
# @project: DesignPattern

from BusinessDelegatePattern.Lookup import BusinessLookUp
from BusinessDelegatePattern.Serviece import BusinessService


# 创建业务代表
class BusinessDelegate:
    lookupService = BusinessLookUp()
    businessService = BusinessService()
    serviceType = ''

    def doTask(self):
        self.businessService = self.lookupService.getBusinessService(self.serviceType)
        self.businessService.doProcessing()
