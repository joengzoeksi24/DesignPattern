# -*- coding:utf-8 -*-
# @time   : 2019-12-20 10:31
# @author : xulei
# @project: DesignPattern


# 类 Employee，该类被当作组合模型类
class Employee:
    def __init__(self, name, dept, salary):
        self._name = name
        self._dept = dept
        self._salary = salary
        self._subordinates = []

    def add(self, e):
        self._subordinates.append(e)

    def remove(self, e):
        self._subordinates.remove(e)

    def getSubordinates(self):
        return self._subordinates

    def __str__(self):
        return "Employee :[ Name: {}, dept: {}, salary: {}]".format(self._name, self._dept, self._salary)
