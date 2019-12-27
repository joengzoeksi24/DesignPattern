# -*- coding:utf-8 -*-
# @time   : 2019-12-27 14:24
# @author : xulei
# @project: DesignPattern

from TransgerObjectPattern.StudentVO import StudentVO


# 创建业务对象
class StudentBO:
    def __init__(self):
        self.students = [StudentVO('Robert', 0), StudentVO('John', 1)]

    def deleteStudent(self, student: StudentVO):
        self.students.remove(student)
        print('Student: Roll No {}, deleted from database.'.format(student.rollNo))

    # 从数据库中检索学生名单
    def getAllStudents(self):
        return self.students

    def getStudent(self, rollNo):
        return self.students[rollNo]

    def updateStudent(self, student: StudentVO):
        self.students[student.rollNo].name = student.name
        print('Student: Roll No {}, updated in the database.'.format(student.rollNo))


