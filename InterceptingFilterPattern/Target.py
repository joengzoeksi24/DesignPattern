# -*- coding:utf-8 -*-
# @time   : 2019-12-27 13:24
# @author : xulei
# @project: DesignPattern


# 创建 Target
class Target:
    def execute(self, request):
        print('Executing request: ', request)
