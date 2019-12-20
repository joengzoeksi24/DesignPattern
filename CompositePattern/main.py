# -*- coding:utf-8 -*-
# @time   : 2019-12-20 10:31
# @author : xulei
# @project: DesignPattern

from CompositePattern.EntityClass import Employee


if __name__ == '__main__':
    CEO = Employee('John', 'CEO', 30000)
    headSales = Employee('Robert', 'Head Sales', 20000)
    headMarketing = Employee('Michel', 'Head Marketing', 20000)
    clerk1 = Employee('Laura', 'Marketing', 10000)
    clerk2 = Employee('Bob', 'Marketing', 10000)
    salesExecutive1 = Employee('Richard', 'Sales', 10000)
    salesExecutive2 = Employee('Rob', 'Sales', 10000)

    CEO.add(headSales)
    CEO.add(headMarketing)

    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)

    headMarketing.add(clerk1)
    headMarketing.add(clerk2)

    print(CEO)
    for h in CEO.getSubordinates():
        print(h)
        for e in h.getSubordinates():
            print(e)
'''
Employee :[ Name: John, dept: CEO, salary: 30000]
Employee :[ Name: Robert, dept: Head Sales, salary: 20000]
Employee :[ Name: Richard, dept: Sales, salary: 10000]
Employee :[ Name: Rob, dept: Sales, salary: 10000]
Employee :[ Name: Michel, dept: Head Marketing, salary: 20000]
Employee :[ Name: Laura, dept: Marketing, salary: 10000]
Employee :[ Name: Bob, dept: Marketing, salary: 10000]
'''
