# -*- coding:utf-8 -*-
# @time   : 2019-12-27 14:24
# @author : xulei
# @project: DesignPattern

from TransgerObjectPattern.StudentBO import StudentBO


if __name__ == '__main__':
    studentBusinessObject = StudentBO()

    # 输出所有学生
    for student in studentBusinessObject.getAllStudents():
        print('Student: [RollNo : {}, Name: {}]'.format(student.rollNo, student.name))

    # 更新学生
    student = studentBusinessObject.getAllStudents()[0]
    student.name = 'Michael'
    studentBusinessObject.updateStudent(student)
    # 获取学生
    student = studentBusinessObject.getStudent(0)
    print('Student: [RollNo: {}, Name: {}]'.format(student.rollNo, student.name))
    '''
    Student: [RollNo : 0, Name: Robert]
    Student: [RollNo : 1, Name: John]
    Student: Roll No 0, updated in the database.
    Student: [RollNo: 0, Name: Michael]
    '''