# 小蓝--中文交互式智能家居机器人(在树莓派raspberrypi上运行)
![Code主要语言](https://img.shields.io/badge/main_code-python-blue.svg)
![Version版本](https://img.shields.io/badge/last_version-V2.0-green.svg)
![build编写进度](https://img.shields.io/badge/first_ver-37%25-brightgreen.svg)
![QQ](https://img.shields.io/badge/QQ-1481605673-yellow.svg)

这是一个中文的智能家居控制对话机器人——由叮当衍生而来，目前还未100%完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验

- 对不起！因为我只是一个刚上初一的小孩，所以如果有任何觉得使用不方便或者错误的地方，希望多多谅解
- 如果大家有点子的话，加我QQ：1481605673，我真诚的邀请您成为小蓝的开发者

## 唤醒词问题：
- 由于本机器人的语音唤醒引擎是snowboy的
- 所以唤醒词英文的会比较准确，所以使用了唤醒词blueberry，比以前的中文唤醒词要好得多，翻译过来就是蓝莓，也没有脱离主题
- 但是snowboy的唤醒词是越多人训练则越准确，所以希望大家在使用小蓝的同时，打开下面的snowboy训练连接，只需要录制三次音频即可
- 网址：https://snowboy.kitt.ai/hotword/20710 （记得录音时说blueberry）
## 介绍本开源项目和WIKI请看：
### https://github.com/xiaoland/xiaolan-dev/wiki
![服务架构](https://github.com/xiaoland/xiaolan-dev/blob/master/%E5%B0%8F%E8%93%9D%E6%9C%8D%E5%8A%A1%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.PNG)


## 更新：（有时间先后顺序）
- 注意：旧的更新在xiaolan-1，这里是小蓝-2
- 小蓝语义理解引擎作为首选语义理解引擎
- 小蓝语义理解引擎大升级，添加槽位识别，追问，意图实时更新系统等
- 小蓝技能移至云端，小蓝大脑移至云端
- 添加讯飞语音识别引擎
- xldo.py改为xiaolan.py
- 改变setting结构
- 改变小蓝结构，分为听觉中枢、语言中枢、记忆中枢、学习中枢、视觉中枢、网络中枢、显示中枢、机械控制中枢、神经网络学习系统
- 添加字典（填充槽位的字典）
- 添加nlp（词法分析，因果关系，情感取向等）
- 添加小蓝云服务器连接接口
- 添加小蓝指令字典和状态字典
- 添加conversation.py专门处理对话
- 添加与小蓝云端服务器对接系统
- 构架好小蓝云端服务器的响应json与客户端请求json和意图列表的list
- 修复小蓝语义理解引擎多个BUG：槽位填充BUG，意图识别BUG
- 将意图列表的[0]和[1]相互对应，意图和关键字相互对应
- 进一步完善小蓝云端-客户端-技能的协议
- 唤醒词升级更新，添加“小度小度”与“jarvis”两个新的唤醒词，都是.umdl（感谢陈果果大大的帮助）
- snowboy引擎升级
- 修复BUG-xiaolanServerCommandsDo
- 代码BUG修复
- 人脸唤醒模式增加
- 添加Log记录
- 添加从数据库读取/写入LOG和一些必要数据
- BUG fix
- 进一步配合云端
- 人脸唤醒BUG修复
- Bug fix
- 小蓝语义理解引擎更新
- 小蓝语义理解引擎
- 小蓝语义理解转移到云端
