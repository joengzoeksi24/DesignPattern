# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:25
# @author : xulei
# @project: DesignPattern

from BusinessDelegatePattern.Delegate import BusinessDelegate


# 创建客户端
class Client:
    def __init__(self, businessService: BusinessDelegate):
        self.businessService = businessService

    def doTask(self):
        self.businessService.doTask()

