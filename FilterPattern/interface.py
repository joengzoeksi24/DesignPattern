# -*- coding:utf-8 -*-
# @time   : 2019-12-19 17:18
# @author : xulei
# @project: DesignPattern

import abc
from FilterPattern.EntityClass import Person


class Criteria(abc.ABC):
    # @abc.abstractmethod
    def meetCriteria(self, persons):
        """"""
        pass
