# -*- coding: utf-8 -*-

import sys
import os
import slotdicts

def intentlistturn():
    return [
            ['weather', ['天气', '天气怎么样', '查询天气', '今天天气'], ['city', slotdicts.dictcity()], 'weather'],
            ['talk', ['我想跟你聊一聊', '我想聊你'], [], 'tuling'],
            ['joke', ['我想听笑话', '笑话', '冷笑话', '给我讲一个笑话'], [], 'joke'],
            ['news', ['我想听新闻', '今天的新闻', '新闻', '今天有什么新闻'], ['newstype', slotdicts.dictnewstype()], 'news'],
            ['smarthome', ['打开', '关闭', '开启', '获取', '传感器', '智能家居'], ['mode', slotdicts.dicthassmode(), 'cortolmode', slotdicts.dicthasscortolmode, 'device', slotdicts.dicthassdevice], 'hass']
            ['camera', ['拍一张照', '给我来一张', '拍照', '拍照'], [], 'camera'],
            ['clock', ['设定一个闹钟', '闹钟', '设置新闹钟', '新建闹钟'], ['day', self.dictday, 'weekday', self.dictweekday, 'hour', self.dicthour, 'minute', self.dictminute], 'clock']
    ]
