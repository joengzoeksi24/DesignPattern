# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:47
# @author : xulei
# @project: DesignPattern

from CompositeEntityPattern.CompositeEntity import CompositeEntity


# 创建使用组合实体的客户端类
class Client:
    compositeEntity = CompositeEntity()

    def printData(self):
        for i in range(len(self.compositeEntity.getData())):
            print('Data: ', self.compositeEntity.getData()[i])

    def setData(self, data1, data2):
        self.compositeEntity.setData(data1, data2)


