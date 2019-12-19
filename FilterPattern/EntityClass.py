# -*- coding:utf-8 -*-
# @time   : 2019-12-19 17:18
# @author : xulei
# @project: DesignPattern


class Person:
    def __init__(self, name, gender, maritalStatus):
        self.name = name
        self.gender = gender
        self.maritalStatus = maritalStatus

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getMaritalStatus(self):
        return self.maritalStatus


from FilterPattern.interface import Criteria


class CriteriaMale(Criteria):
    def meetCriteria(self, persons):
        malePersons = []
        for p in persons:
            if p.getGender() == 'Male':
                malePersons.append(p)
        return malePersons


class CriteriaFemale(Criteria):
    def meetCriteria(self, persons):
        femalePersons = []
        for p in persons:
            if p.getGender() == 'Female':
                femalePersons.append(p)
        return femalePersons


class CriteriaSingle(Criteria):
    def meetCriteria(self, persons):
        singlePersons = []
        for p in persons:
            if p.getMaritalStatus() == 'Single':
                singlePersons.append(p)
        return singlePersons


class AndCriteria(Criteria):
    def __init__(self, criteria, otherCriteria):
        self.criteria = criteria
        self.otherCriteria = otherCriteria

    def meetCriteria(self, persons):
        firstCriteriaPersons = self.criteria.meetCriteria(persons)
        return self.otherCriteria.meetCriteria(firstCriteriaPersons)


class OrCriteria(Criteria):
    def __init__(self, criteria, otherCriteria):
        self.criteria = criteria
        self.otherCriteria = otherCriteria

    def meetCriteria(self, persons):
        firstCriteriaItems = self.criteria.meetCriteria(persons)
        otherCriteriaItems = self.otherCriteria.meetCriteria(persons)

        for po in otherCriteriaItems:
            if po not in firstCriteriaItems:
                firstCriteriaItems.append(po)

        return firstCriteriaItems
