# -*- coding:utf-8 -*-
# @time   : 2019-12-27 09:40
# @author : xulei
# @project: DesignPattern

from FrontControllerPattern.FrontController import FrontController


if __name__ == '__main__':
    frontController = FrontController()
    frontController.dispatchRequest('Home')
    frontController.dispatchRequest('STUDENT')
    '''
    Page requested:  Home
    User is authenticated successfully.
    Displaying Home Page.
    Page requested:  STUDENT
    User is authenticated successfully.
    Displaying Student Page.
    Displaying Home Page.
    '''
