# -*- coding: utf-8 -*-
# 音响控制器
import sys
import os

def ding(): #开始录制指令提示音

    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/ding.wav')

def dong(): #结束录制指令提示音

    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/dong.wav')

def kacha(): #拍照声
    
    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/kacha.mp3')
    
def speak(): #说出的回话
    
    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/say.mp3')

def play(song_name): #音乐播放器
    
    print('正在播放:' + song_name)
    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/music.mp3')

def stop():

    try:
        sys.exit(-1)
    except:
        os.system('python /home/pi/auditory_center/awaken/snowboy.py')

def speacilrecorder():

    os.system('mplayer /home/pi/xiaolan/memory_center/musiclib/speacilrecorder.mp3')
    
def DiyOmxSpeaker(outputdevice, fileroad):
    
    os.system('omxplayer -r -o ' + outputdevice +  ' ' + fileroad)
    
def DiyMplayerSpeaker(fileroad):
    
    os.system('mplayer ' + fileroad)
