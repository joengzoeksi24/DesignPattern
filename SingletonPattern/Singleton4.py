# -*- coding:utf-8 -*-
# @time   : 2019-12-12 16:09
# @author : xulei
# @project: DesignPattern


"""
方法4：方法1的升级/高级版本
使用装饰器decorator，
这是一种更pythonic，更elegant的方法，
单例类本身根据不知道自己是单例的，因为他本身（自己的代码）并不是单例的
"""


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    one = MyClass()  # one和two是完全相同的
    two = MyClass()
    two.a = 3
    print(one.a)
    print(id(one), id(two))
    print(one == two)
    print(one is two)
    one.x = 1
    print(one.x, two.x)
'''
3
139912758322064 139912758322064
True
True
1 1
'''