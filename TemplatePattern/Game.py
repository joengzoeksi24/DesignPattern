# -*- coding:utf-8 -*-
# @time   : 2019-12-26 09:37
# @author : xulei
# @project: DesignPattern

import abc


# 创建一个抽象类，它的模板方法被设置为 final
class Game(abc.ABC):
    print('Game!!!')

    def __new__(cls, *args, **kwargs):
        print('Game __new__!!!')
        if cls != Game and 'play' in cls.__dict__.keys():
            raise Exception('This method cannot be rewritten.')
        else:
            return super(Game, cls).__new__(cls, *args, **kwargs)

    @abc.abstractmethod
    def initialize(self):
        """"""

    @abc.abstractmethod
    def startPlay(self):
        """"""

    @abc.abstractmethod
    def endPlay(self):
        """"""

    def play(self):  # final，子类不可以重写
        print('Game play!!!')
        self.initialize()
        self.startPlay()
        self.endPlay()


class Cricket(Game):
    print('Cricket!!!')

    def endPlay(self):
        print('Cricket Game Finished!')

    def initialize(self):
        print('Cricket Game Initialized! Start playing.')

    def startPlay(self):
        print('Cricket Game Started. Enjoy the game!')


class Football(Game):
    def endPlay(self):
        print('Football Game Finished!')

    def initialize(self):
        print('Football Game Initialized! Start playing.')

    def startPlay(self):
        print('Football Game Started. Enjoy the game!')

    # def play(self):
    #     print('Football Game play.')


if __name__ == '__main__':
    print(Game.__dir__)
    print(Game.__dict__)
    print(Game.__dict__.keys())
    '''
    <method '__dir__' of 'object' objects>
    {'__module__': '__main__', 'initialize': <function Game.initialize at 0x7fd39f0f3510>, 'startPlay': <function Game.startPlay at 0x7fd39f0f3f28>, 'endPlay': <function Game.endPlay at 0x7fd39f11f048>, 'play': <function Game.play at 0x7fd39f11f0d0>, '__doc__': None, '__abstractmethods__': frozenset({'initialize', 'endPlay', 'startPlay'}), '_abc_registry': <_weakrefset.WeakSet object at 0x7fd3a06b44a8>, '_abc_cache': <_weakrefset.WeakSet object at 0x7fd39f0f7f98>, '_abc_negative_cache': <_weakrefset.WeakSet object at 0x7fd39f1080b8>, '_abc_negative_cache_version': 35}
    dict_keys(['__module__', 'initialize', 'startPlay', 'endPlay', 'play', '__doc__', '__abstractmethods__', '_abc_registry', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version'])
    '''
    print()
    football = Football()
    '''
    Exception: This method cannot be rewritten.
    '''