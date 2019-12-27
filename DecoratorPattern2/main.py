# -*- coding:utf-8 -*-
# @time   : 2019-12-23 10:26
# @author : xulei
# @project: DesignPattern

"""
1.装饰器是让你在一个函数的前后去执行代码。
2.@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
3.装饰器是类，装饰器类
参考： https://www.runoob.com/w3cnote/python-func-decorators.html
"""

from functools import wraps


# 创建装饰器类
class decorator_setRedBorder(object):
    print('decorator_setRedBorder')

    def __call__(self, func):
        @wraps(func)
        def decorated():
            print('I am doing some boring work before executing func()')
            print('Border Color: Red')
            func()
            print('I am doing some boring work after executing func()')
        return decorated


# 带参数的装饰器类
class decorator_TextColor:
    print('decorator_TextColor')

    def __init__(self, pro='black'):
        self.pro = pro

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            print('Text Color: {}'.format(self.pro))
            func(*args, **kwargs)
            # return func(*args, **kwargs)  # 这样也可以
        return decorated


# 实体函数
@decorator_setRedBorder()
def drawRectangle():
    print('Shape: Rectangle')


@decorator_TextColor('green')
def drawCircle():
    print('Shape: Circle')


@decorator_TextColor()
def drawShape1(shape):
    print('Shape: {}'.format(shape))


if __name__ == '__main__':
    drawRectangle()
    print()
    drawCircle()
    print()
    drawShape1('Circle')
    print()
    '''
    decorator_setRedBorder
    decorator_TextColor
    I am doing some boring work before executing func()
    Border Color: Red
    Shape: Rectangle
    I am doing some boring work after executing func()
    
    Text Color: green
    Shape: Circle
    
    Text Color: black
    Shape: Circle
    '''