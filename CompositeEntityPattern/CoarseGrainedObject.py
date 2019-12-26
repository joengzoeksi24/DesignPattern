# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:47
# @author : xulei
# @project: DesignPattern

from CompositeEntityPattern.DependentObject import DependentObject1, DependentObject2


# 创建粗粒度对象
class CoarseGrainedObject:
    do1 = DependentObject1()
    do2 = DependentObject2()

    def setData(self, data1, data2):
        self.do1.data = data1
        self.do2.data = data2

    def getData(self):
        return [self.do1.data, self.do2.data]