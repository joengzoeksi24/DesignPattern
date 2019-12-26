# -*- coding:utf-8 -*-
# @time   : 2019-12-26 09:37
# @author : xulei
# @project: DesignPattern

from TemplatePattern.Game import Cricket, Football


if __name__ == '__main__':
    game = Cricket()
    game.play()
    print()
    game = Football()
    game.play()
    '''
    Game!!!
    Cricket!!!
    Game __new__!!!
    Game play!!!
    Cricket Game Initialized! Start playing.
    Cricket Game Started. Enjoy the game!
    Cricket Game Finished!
    
    Game __new__!!!
    Game play!!!
    Football Game Initialized! Start playing.
    Football Game Started. Enjoy the game!
    Football Game Finished!
    '''
