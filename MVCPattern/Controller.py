# -*- coding:utf-8 -*-
# @time   : 2019-12-26 11:16
# @author : xulei
# @project: DesignPattern


# 创建控制器
class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setStudentName(self, name):
        self.model.name = name

    def getStudentName(self):
        return self.model.name

    def setStudentRollNo(self, rollNo):
        self.model.rollNo = rollNo

    def getStudentRollNo(self):
        return self.model.rollNo

    def updateView(self):
        self.view.printStudentDetails(self.model.name, self.model.rollNo)

