# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:20
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Packing import Packing


# 实现Packing接口的实体类
class Bottle(Packing):
    def pack(self):
        return "Bottle"
