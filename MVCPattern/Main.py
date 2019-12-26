# -*- coding:utf-8 -*-
# @time   : 2019-12-26 11:16
# @author : xulei
# @project: DesignPattern

from MVCPattern.Model import Student
from MVCPattern.View import StudentView
from MVCPattern.Controller import StudentController


def retrieveStudentFromDatabase():
    student = Student()
    student.name = 'Robert'
    student.rollNo = '10'
    return student


if __name__ == '__main__':
    # 从数据库获取学生记录
    model = retrieveStudentFromDatabase()
    # 创建一个视图：把学生详细信息输出到控制台
    view = StudentView()
    controller = StudentController(model, view)
    controller.updateView()
    print()
    # 更新模型数据
    controller.setStudentName('John')
    controller.updateView()
'''
Student: 
Name:  Robert
Roll No:  10

Student: 
Name:  John
Roll No:  10
'''

