# -*- coding:utf-8 -*-
# @time   : 2019-12-23 14:53
# @author : xulei
# @project: DesignPattern

from ProxyPattern.interface import Image


# 创建实现接口的实体类
class RealImage(Image):
    def __init__(self, fileName):
        self.fileName = fileName
        self.loadFromDisk(fileName)

    def display(self):
        print('Displaying ', self.fileName)

    def loadFromDisk(self, fileName):
        print('Loading ', fileName)


class ProxyImage(Image):
    realImage = None

    def __init__(self, fileName):
        self.fileName = fileName

    def display(self):
        if self.realImage is None:
            self.realImage = RealImage(self.fileName)
        self.realImage.display()
