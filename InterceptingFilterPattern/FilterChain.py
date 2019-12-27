# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:24
# @author : xulei
# @project: DesignPattern

from InterceptingFilterPattern.Target import Target


# 创建过滤器链
class FilterChain:
    filters = []
    target = Target()

    def addFilter(self, filter):
        self.filters.append(filter)

    def execute(self, request):
        for filter in self.filters:
            filter.execute(request)
        self.target.execute(request)

    def setTarget(self, target):
        self.target = target

