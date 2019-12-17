# -*- coding:utf-8 -*-
# @time   : 2019-12-17 13:31
# @author : xulei
# @project: DesignPattern

from AdapterPattern.EntityClass import AudioPlayer


if __name__ == '__main__':
    audioPlayer = AudioPlayer()
    audioPlayer.play('mp3', 'beyond the horizon.mp3')
    audioPlayer.play('mp4', 'alone.mp4')
    audioPlayer.play('vlc', 'far far away.vlc')
    audioPlayer.play('avi', 'mind me.avi')
'''
playing mp3 file.name: beyond the horizon.mp3
playing mp4 file.name: alone.mp4
playing vlc file.name: far far away.vlc
invalid media. avi format not supported
'''
