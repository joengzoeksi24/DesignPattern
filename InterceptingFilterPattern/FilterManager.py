# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:24
# @author : xulei
# @project: DesignPattern

from InterceptingFilterPattern.FilterChain import FilterChain


# 创建过滤管理器
class FilterManager:
    def __init__(self, target):
        self.filterChain = FilterChain()
        self.filterChain.setTarget(target)

    def setFilter(self, filter):
        self.filterChain.addFilter(filter)

    def filterRequest(self, request):
        self.filterChain.execute(request)


