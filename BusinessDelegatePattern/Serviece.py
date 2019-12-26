# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:24
# @author : xulei
# @project: DesignPattern

import abc


# 创建 BusinessService 接口
class BusinessService(abc.ABC):
    def doProcessing(self):
        """"""


# 创建实体服务类
class EJBService(BusinessService):
    def doProcessing(self):
        print('Processing task by invoking EJB Service.')


class JMSService(BusinessService):
    def doProcessing(self):
        print('Processing task by invoking JMS Service.')



