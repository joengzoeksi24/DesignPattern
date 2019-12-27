# -*- coding:utf-8 -*-
# @time   : 2019-12-27 09:40
# @author : xulei
# @project: DesignPattern

from FrontControllerPattern.Views import StudentView, HomeView


# 创建调度器 Dispatcher
class Dispatcher:
    def __init__(self):
        self.studentView = StudentView()
        self.homeView = HomeView()

    def dispatch(self, request: str):
        if request.lower() == 'student':
            self.studentView.show()
        self.homeView.show()
