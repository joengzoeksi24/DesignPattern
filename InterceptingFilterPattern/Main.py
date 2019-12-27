# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:25
# @author : xulei
# @project: DesignPattern

from InterceptingFilterPattern.FilterManager import FilterManager
from InterceptingFilterPattern.Client import Client
from InterceptingFilterPattern.Filter import AuthenticationFilter, DebugFilter
from InterceptingFilterPattern.Target import Target


# 使用 Client 来演示拦截过滤器设计模式
if __name__ == '__main__':
    filterManager = FilterManager(Target())
    filterManager.setFilter(AuthenticationFilter())
    filterManager.setFilter(DebugFilter())

    client = Client()
    client.setFilterManager(filterManager)
    client.sendRequest('HOME')
    '''
    Authenticating request:  HOME
    request log:  HOME
    Executing request:  HOME
    '''