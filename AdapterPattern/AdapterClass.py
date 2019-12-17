# -*- coding:utf-8 -*-
# @time   : 2019-12-17 13:18
# @author : xulei
# @project: DesignPattern

from AdapterPattern.interface import MediaPlayer
from AdapterPattern.EntityClass import V1cPlayer, Mp4Player


# 创建实现了 MediaPlayer 接口的适配器类
class MediaAdapter(MediaPlayer):

    def __init__(self, audioType):
        self.advancedMusicPlayer = None
        if audioType == 'vlc':
            self.advancedMusicPlayer = V1cPlayer()
        elif audioType == 'mp4':
            self.advancedMusicPlayer = Mp4Player()

    def play(self, audioType, fileName):
        if audioType == 'vlc':
            self.advancedMusicPlayer.playV1c(fileName)
        elif audioType == 'mp4':
            self.advancedMusicPlayer.playMp4(fileName)


