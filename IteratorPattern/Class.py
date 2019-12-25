# -*- coding:utf-8 -*-
# @time   : 2019-12-25 09:22
# @author : xulei
# @project: DesignPattern

from IteratorPattern.interface import Container,Iterator


# 创建实现了 Container 接口的实体类。该类有实现了 Iterator 接口的内部类 NameIterator
class NameRepository(Container):
    names = ["Robert", "John","Julie", "Lora"]

    def getIterator(self):
        return self.NameIterator()

    class NameIterator(Iterator):
        index = 0

        def hasNext(self):
            if self.index < len(NameRepository.names):
                return True
            return False

        def next(self):
            if self.hasNext():
                value = NameRepository.names[self.index]
                self.index += 1
                return value
            # return None
