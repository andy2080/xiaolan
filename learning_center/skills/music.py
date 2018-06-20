# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
import random
sys.path.append('/home/pi/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

def start(tok):
    m = xlMusic()
    m.main(tok)

class xlMusic(object):
    
    def __init__(self):
        
        pass
    
    def command_choose(self, commands, tok):
        
        if '随机播放' in commands or '随机' in commands:
            m.sui_ji(services, tok)
        elif '搜索播放' in commands or '搜索' in commands:
            try:
                m.sou_suo(services, commands[-1:-4], tok)
            except KeyError:
                m.sou_suo(services, '', tok)
        elif '歌名' in commands or '这首歌叫什么' in commands:
            command = 'song_name_q'
            return command
        elif '退出' in commands:
            bt.tts('谢谢使用，下次再见', tok)
            speaker.speak()
            try:
                sys.exit(-1)
            except SystemExit:
                os.system('python /home/pi/xiaolan/snowboy.py')
        else:
            bt.tts('对不起，我没有听清楚您说了什么？', tok)
            speaker.speak()
            m.main(tok)
    
    def paly(self, song_name, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        while song_name != None:
            speaker.play()
            bt.tts('请问还要听什么吗？可以输入指令，如，这首歌叫什么，或者，搜索歌曲', tok)
            speaker.speak()
            speaker.ding()
            r.record()
            speaker.dong()
            m.command_choose(bs.stt('./voice.wav', tok), tok)
        else:
            bt.tts('对不起，发生了故障', tok)
            speaker.speak()
    
    def sou_suo(self, services, song_name, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
        
        if song_name == '' or song_name == None:
            bt.tts('请问您要听什么歌?', tok)
            speaker.speak()
            speaker.ding()
            r.record()
            speaker.dong()
            song_name = bs.stt('./voice.wav', tok)
        else:
            get_song_id_rawj = requests.get(url + services['search'] + song_name)
            get_song_id_j = get_song_id_rawj.json()
            try:
                id = get_song_id_j['song'][song_name_c]['songid']
            except KeyError:
                try:
                    id = get_song_id_j['song'][0]['songid']
                except KeyError:
                    bt.tts('对不起，歌曲获取失败')
                    speaker.speak()
                else:
                    pass
            else:
                get_song_url_rawj = requests.get(url + services['musicurl_get'] + id)
                get_song_url_j = get_song_url_rawj.json()
                
                song_name = get_song_url_j['songinfo']['title']
                song_url = (get_song_url_j['bitrate']['file_link'].replace('\', '''))
                
                download = requests.get(song_url)
                with open("/home/pi/xiaolan/musiclib/music.mp3", "wb") as code:
                    code.write(download.content)
                
                m.play(song_name, tok)
    
    def sui_ji(self, services, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
        song_name_c = random.uniform(0, 12)
        song_name_s = ['皮皮虾我们走','I hope you think of me','小幸运','全部都是你','佛系少女','Something just like this',
                       'Feel this Moment','Welcome to NewYork','洛天依投食歌','带你去旅行','死机之歌','Shape of You','Kiss Fight',
                       'Hot song']

        if song_name_s[random.uniform(0, 12)] != 'Hot song':
            get_song_id_rawj = requests.get(url + services['search'] + song_name_c)
        else:
            get_song_id_rawj = requests.get(url + services['hot'])
        get_song_id_j = get_song_id_rawj.json()
        
        try:
            if song_name_s[random.uniform(0, 12)] == 'Hot song':
                id = get_song_id_j['result']['list'][song_name_c]['song_id']
            else:
                id = get_song_id_j['song'][song_name_c]['songid']
        except KeyError:
            try:
                if song_name == 'Hot song':
                    id = get_song_id_j['result']['list'][song_name_c]['song_id']
                else:
                    id = get_song_id_j['song'][song_name_c]['songid']
            except KeyError:
                bt.tts('对不起，播放错误')
                speaker.speak()
            else:
                pass
        
        else:
            get_song_url_rawj = requests.get(url + services['musicurl_get'] + id)
            get_song_url_j = get_song_url_rawj.json()
            
            song_name = get_song_url_j['songinfo']['title']
            song_url_f = get_song_url_j['bitrate']['file_link']
            song_url = (song_url_f.replace('\', '''))
            
            download = requests.get(song_url)
            with open("/home/pi/xiaolan/musiclib/music.mp3", "wb") as code:
                code.write(download.content)
            
            m.play(song_name, tok)
        
    def main(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
        services = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
        
        bt.tts('欢迎使用小蓝音乐播放器，云服务使用百度音乐', tok)
        speaker.speak()
        bt.tts('请问您要随机播放还是搜索播放？', tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        
        try:
            commands = bs.stt('./voice.wav', tok)
            m.command_choose(commands, tok)
        except TypeError:
            speaker.speak()
            speaker.ding()
            r.record()
            speaker.dong()
            m.command_choose(commands, tok)
                
