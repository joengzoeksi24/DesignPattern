# -*- coding:utf-8 -*-
# @time   : 2019-12-27 09:39
# @author : xulei
# @project: DesignPattern

from FrontControllerPattern.Dispatcher import Dispatcher


# 创建前端控制器 FrontController
class FrontController:
    def __init__(self):
        self.dispatcher = Dispatcher()

    @staticmethod  # 能够被类和对象调用，但参数不能为self和cls，因此不能访问对象和类的属性
    def isAuthenticUser():
        print('User is authenticated successfully.')
        return True

    @staticmethod
    def trackRequest(request):
        print('Page requested: ', request)

    def dispatchRequest(self, request):
        # 记录每一个请求
        self.trackRequest(request)
        # 对用户进行身份验证
        if self.isAuthenticUser():
            self.dispatcher.dispatch(request)