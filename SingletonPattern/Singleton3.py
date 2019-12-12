# -*- coding:utf-8 -*-
# @time   : 2019-12-12 16:00
# @author : xulei
# @project: DesignPattern


"""???
方法3：本质上是方法1的升级或者说是高级版
使用__metaclass__（元类）的高级Python用法
"""


class Singleton(type):
    def __init__(self, cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(self, cls, *args, **kwargs):
        """ Call self as a function. """
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class MyClass(object):
    a = 1
    __metaclass__ = Singleton


if __name__ == '__main__':
    one = MyClass()  # one和two是两个不同的对象
    two = MyClass()
    two.a = 3
    print(one.a)
    print(id(one), id(two))
    print(one == two)
    print(one is two)
'''
1
139725368918088 139725368919488
False
False
'''