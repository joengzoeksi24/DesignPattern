# -*- coding:utf-8 -*-
# @time   : 2019-12-17 11:36
# @author : xulei
# @project: DesignPattern

import abc


# 为媒体播放器创建接口
class MediaPlayer(abc.ABC):
    @abc.abstractmethod
    def play(self, audioType, fileName):
        """"""


# 为更高级的媒体播放器创建接口
class AdvanceMediaPlayer(abc.ABC):
    @abc.abstractmethod
    def playV1c(self, fileName):
        """"""
    @abc.abstractmethod
    def playMp4(self, fileName):
        """"""
