# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:24
# @author : xulei
# @project: DesignPattern

import abc


# 创建过滤器接口 Filter
class Filter(abc.ABC):
    def execute(self, request):
        """"""


# 创建实体过滤器
class AuthenticationFilter(Filter):
    def execute(self, request):
        print('Authenticating request: ', request)


class DebugFilter(Filter):
    def execute(self, request):
        print('request log: ', request)

