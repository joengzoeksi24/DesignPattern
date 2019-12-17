# -*- coding:utf-8 -*-
# @time   : 2019-12-17 13:13
# @author : xulei
# @project: DesignPattern

from AdapterPattern.interface import MediaPlayer,AdvanceMediaPlayer


# 创建实现了 AdvancedMediaPlayer 接口的实体类
class V1cPlayer(AdvanceMediaPlayer):
    def playV1c(self, fileName):
        print('playing vlc file.name:', fileName)

    def playMp4(self, fileName):
        """"""


class Mp4Player(AdvanceMediaPlayer):
    def playV1c(self, fileName):
        """"""

    def playMp4(self, fileName):
        print('playing mp4 file.name:', fileName)


from AdapterPattern.AdapterClass import MediaAdapter


# 创建实现了 MediaPlayer 接口的实体类
class AudioPlayer(MediaPlayer):
    def play(self, audioType, fileName):
        if audioType == 'mp3':  # 播放 mp3 音乐文件的内置支持
            print('playing mp3 file.name:', fileName)
        elif audioType == 'vlc' or audioType == 'mp4':
            mediaAdapter = MediaAdapter(audioType)
            mediaAdapter.play(audioType, fileName)
        else:
            print('invalid media. {} format not supported'.format(audioType))
