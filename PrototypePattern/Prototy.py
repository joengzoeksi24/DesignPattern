# -*- coding:utf-8 -*-
# @time   : 2019-12-16 11:03
# @author : xulei
# @project: DesignPattern

import copy

# 拷贝接口
class ICloneable:

    def shallowClone(self):
        return copy.copy(self)

    def deepClone(self):
        return copy.deepcopy(self)


# 工作经历
class WorkExperience(ICloneable):
    wordData = ''
    company = ''
    pass


# 简历
class Resume(ICloneable):
    name = ''
    sex = '未知'
    age = 0
    work = None

    def __init__(self, name, work = WorkExperience()):
        self.name = name
        self.work = work

    def setPersonInfo(self, sex, age):
        self.sex = sex
        self.age = age

    def setWorkExperience(self, workData, company):
        self.work.wordData = workData
        self.work.company = company

    def display(self):
        print(self.name, self.sex, self.age)
        print(self.work.wordData, self.work.company)


def clientUI():
    a = Resume('xl')
    a.setPersonInfo('女', 26)
    a.setWorkExperience("2018-2019", 'xx公司')

    # 浅拷贝
    b = a.shallowClone()
    b.setWorkExperience('2019-2020', 'yy公司')

    # 深拷贝
    c = a.deepClone()
    c.setWorkExperience('2017-2020', 'zz公司')

    print(a)
    a.display()
    print(b)
    b.display()
    print(c)
    c.display()


if __name__ == '__main__':
    clientUI()

'''
<__main__.Resume object at 0x7fb468aac8d0>
xl 女 26
2019-2020 yy公司
<__main__.Resume object at 0x7fb468aac978>
xl 女 26
2019-2020 yy公司
<__main__.Resume object at 0x7fb468aace48>
xl 女 26
2017-2020 zz公司
'''