# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:47
# @author : xulei
# @project: DesignPattern

from CompositeEntityPattern.CoarseGrainedObject import CoarseGrainedObject


# 创建组合实体
class CompositeEntity:
    cgo = CoarseGrainedObject()

    def setData(self, data1, data2):
        self.cgo.setData(data1, data2)

    def getData(self):
        return self.cgo.getData()