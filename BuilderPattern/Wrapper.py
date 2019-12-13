# -*- coding:utf-8 -*-
# @time   : 2019-12-13 15:19
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Packing import Packing


# 实现Packing接口的实体类
class Wrapper(Packing):
    def pack(self):
        return "Wrapper"
