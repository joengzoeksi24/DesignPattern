# -*- coding:utf-8 -*-
# @time   : 2019-12-26 13:25
# @author : xulei
# @project: DesignPattern

from BusinessDelegatePattern.Client import Client, BusinessDelegate


if __name__ == '__main__':
    businessDelegate = BusinessDelegate()
    businessDelegate.serviceType = 'EJB'

    client = Client(businessDelegate)
    client.doTask()

    businessDelegate.serviceType = 'JMS'
    client.doTask()
    '''
    Processing task by invoking EJB Service.
    Processing task by invoking JMS Service.
    '''