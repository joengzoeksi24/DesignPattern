# -*- coding:utf-8 -*-
# @time   : 2019-12-27 08:49
# @author : xulei
# @project: DesignPattern

from DataAccessObjectPattern.StudentDao import StudentDaoImpl


if __name__ == '__main__':
    studentDao = StudentDaoImpl()

    # 输出所有的学生
    for student in studentDao.getAllStudent():
        print('Student: [RollNo: {}, Name: {}]'.format(student.rollNo, student.name))

    # 更新学生
    student0 = studentDao.getAllStudent()[0]
    student0.name = 'Michael'
    studentDao.updateStudent(student0)

    # 获取学生
    student0 = studentDao.getStudent(0)
    print('Student: [RollNo: {}, Name: {}]'.format(student0.rollNo, student0.name))
'''
Student: [RollNo: 0, Name: Robert]
Student: [RollNo: 1, Name: John]
Student: Roll No 0, updated in the database.
Student: [RollNo: 0, Name: Michael]
'''