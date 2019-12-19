# -*- coding:utf-8 -*-
# @time   : 2019-12-19 17:18
# @author : xulei
# @project: DesignPattern

"""
将创建一个 Person 对象、Criteria 接口和实现了该接口的实体类，来过滤 Person 对象的列表。CriteriaPatternDemo，我们的演示类使用 Criteria 对象，基于各种标准和它们的结合来过滤 Person 对象的列表。
"""

from FilterPattern.EntityClass import Person, CriteriaMale, CriteriaFemale, CriteriaSingle, AndCriteria, OrCriteria


def printPersons(persons):
    for p in persons:
        # print('p: ', p)
        print("person:[name: {}, gender: {}, marital status: {}]".format(p.getName(), p.getGender(), p.getMaritalStatus()))


if __name__ == '__main__':
    persons = []
    persons.extend([Person("Robert", "Male", "Single"),
                   Person("John", "Male", "Married"),
                   Person("Laura", "Female", "Married"),
                   Person("Diana", "Female", "Single"),
                   Person("Mike", "Male", "Single"),
                   Person("Bobby", "Male", "Single")])
    print('persons: ', len(persons), persons)
    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    singleMale = AndCriteria(single, male)
    singleOrFemale = OrCriteria(single, female)
    print('males: ')
    # print(male.meetCriteria(persons))
    printPersons(male.meetCriteria(persons))
    print('females: ')
    printPersons(female.meetCriteria(persons))
    print('single males: ')
    printPersons(singleMale.meetCriteria(persons))
    print('single or females: ')
    printPersons(singleOrFemale.meetCriteria(persons))
    '''
    males: 
    person:[name: Robert, gender: Male, marital status: Single]
    person:[name: John, gender: Male, marital status: Married]
    person:[name: Mike, gender: Male, marital status: Single]
    person:[name: Bobby, gender: Male, marital status: Single]
    females: 
    person:[name: Laura, gender: Female, marital status: Married]
    person:[name: Diana, gender: Female, marital status: Single]
    single males: 
    person:[name: Robert, gender: Male, marital status: Single]
    person:[name: Mike, gender: Male, marital status: Single]
    person:[name: Bobby, gender: Male, marital status: Single]
    single or females: 
    person:[name: Robert, gender: Male, marital status: Single]
    person:[name: Diana, gender: Female, marital status: Single]
    person:[name: Mike, gender: Male, marital status: Single]
    person:[name: Bobby, gender: Male, marital status: Single]
    person:[name: Laura, gender: Female, marital status: Married]
    '''