# -*- coding:utf-8 -*-
# @time   : 2019-12-12 15:45
# @author : xulei
# @project: DesignPattern


"""
方法1：实现__new__方法
并在将一个类的实例绑定到类变量_instance上，
如果cls._instance为None说明该类还没有实例化过，实例化该类，并返回
如果cls._instance不为None，直接返回cls._instance
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    a = 1


if __name__ == '__main__':
    one = MyClass()  # one和two是完全相同的
    two = MyClass()
    two.a = 3
    print(one.a)
    print(id(one), id(two))
    print(one == two)
    print(one is two)
'''
3
140243830707704 140243830707704
True
True
'''