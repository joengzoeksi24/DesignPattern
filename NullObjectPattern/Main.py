# -*- coding:utf-8 -*-
# @time   : 2019-12-25 13:32
# @author : xulei
# @project: DesignPattern

from NullObjectPattern.Factory import CustomerFactory


# 使用 CustomerFactory，基于客户传递的名字，来获取 RealCustomer 或 NullCustomer 对象
if __name__ == '__main__':
    customer1 = CustomerFactory().getCustomer('Rob')
    customer2 = CustomerFactory().getCustomer('Bob')
    customer3 = CustomerFactory().getCustomer('Julie')
    customer4 = CustomerFactory().getCustomer('Laura')

    print('Customers')
    print(customer1.getName())
    print(customer2.getName())
    print(customer3.getName())
    print(customer4.getName())
    '''
    Customers
    Rob
    Not Available in Customer Database
    Julie
    Not Available in Customer Database
    '''