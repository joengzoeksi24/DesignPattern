# -*- coding:utf-8 -*-
# @time   : 2019-12-23 14:53
# @author : xulei
# @project: DesignPattern

from ProxyPattern.Class import ProxyImage


# 当被请求时，使用 ProxyImage 来获取 RealImage 类的对象
if __name__ == '__main__':
    image = ProxyImage('./test.jpg')
    # 图像将从磁盘加载
    image.display()
    print()
    # 图像不需要从磁盘加载
    image.display()
    '''
    Loading  ./test.jpg
    Displaying  ./test.jpg
    
    Displaying  ./test.jpg
    '''