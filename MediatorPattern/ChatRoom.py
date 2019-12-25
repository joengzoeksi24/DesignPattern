# -*- coding:utf-8 -*-
# @time   : 2019-12-25 10:05
# @author : xulei
# @project: DesignPattern

from datetime import datetime


# 创建中介类
class CharRoom:
    @classmethod
    def showMessage(self, user, message):
        print(str(datetime.now()), ' [{}]: {}'.format(user.name, message))
