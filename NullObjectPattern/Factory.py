# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:32
# @author : xulei
# @project: DesignPattern

from NullObjectPattern.Customer import NullCustomer, RealCustomer


class CustomerFactory:
    names = ["Rob", "Joe", "Julie"]

    def getCustomer(self, name):
        for namei in self.names:
            if name == namei:
                return RealCustomer(name)

        return NullCustomer()
