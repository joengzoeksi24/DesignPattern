# -*- coding:utf-8 -*-
# @time   : 2019-12-12 16:28
# @author : xulei
# @project: DesignPattern


class Singleton:
    a = 1
    _instance = None

    def getInstance(self):
        if self._instance is None:
            _instance = Singleton()
        return _instance

    def show(self):
        print("hello Singleton!!!")


if __name__ == '__main__':
    one = Singleton().getInstance()  # one和two是两个不同的对象
    two = Singleton().getInstance()
    one.show()
    two.show()
    two.a = 3
    print(one.a)
    print(id(one), id(two))
    print(one == two)
    print(one is two)
'''
hello Singleton!!!
hello Singleton!!!
1
139754833739848 139754833741248
False
False
'''