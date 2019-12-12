# -*- coding:utf-8 -*-
# @time   : 2019-12-12 15:52
# @author : xulei
# @project: DesignPattern


"""
方法2：共享属性：所谓单例就是所有引用（实例、对象）拥有相同的状态（属性）和行为（方法）
同一个类的所有实例天然拥有相同的行为（方法）
只需要保证同一个类的所有实例具有相同的状态（属性）即可
所有实例共享属性的最简单最直接的方法就是__dict__属性指向（引用）同一个字典（dict）
"""


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls)
        ob.__dict__ = cls._state
        return ob


class MyClass(Singleton):
    a = 1


if __name__ == '__main__':
    one = MyClass()  # one和two是两个不同的对象，但是具有相同的（同一个__dict__属性）
    two = MyClass()
    two.a = 3
    print(one.a)
    print(id(one), id(two))
    print(one == two)
    print(one is two)
    print(id(one.__dict__), id(two.__dict__))
'''
3
140406314857920 140406314857416
False
False
140421697291536 140421697291536
'''