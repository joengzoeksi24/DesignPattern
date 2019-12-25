# -*- coding:utf-8 -*-
# @time   : 2019-12-25 10:05
# @author : xulei
# @project: DesignPattern

from MediatorPattern.ChatRoom import CharRoom


class User:
    name = ''

    def __init__(self, name):
        self.name = name

    def sendMessage(self, message):
        CharRoom.showMessage(self, message)
