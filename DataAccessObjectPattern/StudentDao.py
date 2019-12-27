# -*- coding:utf-8 -*-
# @time   : 2019-12-27 08:49
# @author : xulei
# @project: DesignPattern

import abc
from DataAccessObjectPattern.Student import Student


# 创建数据访问对象接口
class StudentDao(abc.ABC):
    def getAllStudent(self):
        """"""

    def getStudent(self, rollNo):
        """"""

    def updateStudent(self, student):
        """"""

    def deleteStudent(self, student):
        """"""


# 创建实现了上述接口的实体类
class StudentDaoImpl(StudentDao):
    students = []

    def __init__(self):
        self.students.append(Student('Robert', 0))
        self.students.append(Student('John', 1))

    def deleteStudent(self, student):
        self.students.remove(student.rollNo)
        print('Student: Roll No {}, deleted from database.'.format(student.rollNo))

    # 从数据库中检索学生名单
    def getAllStudent(self):
        return self.students

    def getStudent(self, rollNo):
        return self.students[rollNo]

    def updateStudent(self, student):
        self.students[student.rollNo].name = student.name
        print('Student: Roll No {}, updated in the database.'.format(student.rollNo))
