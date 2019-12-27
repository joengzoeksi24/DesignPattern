# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:25
# @author : xulei
# @project: DesignPattern

from InterceptingFilterPattern.FilterManager import FilterManager


# 创建客户端 Client
class Client:
    filterManager = None

    def setFilterManager(self, filterManager: FilterManager):
        self.filterManager = filterManager

    def sendRequest(self, request):
        self.filterManager.filterRequest(request)