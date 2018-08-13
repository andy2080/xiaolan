# 小蓝--智能家居语音交互式人工智能机器人(在树莓派上运行)
![Code主要语言](https://img.shields.io/badge/main_code-python-blue.svg)
![Version版本](https://img.shields.io/badge/last_version-V2.0-green.svg)
![build编写进度](https://img.shields.io/badge/first_ver-37%25-brightgreen.svg)
![WeChat](https://img.shields.io/badge/WeChat-18680171381-orange.svg)
![QQ](https://img.shields.io/badge/QQ-1481605673-yellow.svg)

# 很抱歉，小蓝现在将源代码移植到了腾讯的工蜂上，如果有人愿意一起开发，那么请加我QQ：1481605673或者微信18680171381

- 对不起！因为我只是一个准备上初二的小孩，所以如果有任何觉得使用不方便或者错误的地方，希望多多谅解
- 如果大家有点子的话，加我QQ：1481605673，我真诚的邀请您成为小蓝的开发者

## 唤醒词问题：
- 根据百度的唤醒词测试，得出“小蓝小蓝”并不适合作为唤醒词，所以更换为五星的“小蓝同学”作为预训练唤醒词
- 目前默认唤醒词依然为“jarvis”

## 小蓝的WIKI和安装请看：
### https://github.com/xiaoland/xiaolan/wiki
![服务架构](https://github.com/xiaoland/xiaolan/blob/master/%E5%B0%8F%E8%93%9D%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE2.PNG)


## 注意问题：
- 如果您要使用人脸唤醒，那么请先设置setting.py里的main_setting的awaken为face，然后请看visual_centre下面的人脸唤醒必读.txt


## 下载&使用：
- git clone https://github.com/xiaoland/xiaolan.git xiaolan
- cd xiaolan
- cd memory_center/more
- su root（没有解锁root的请sudo passwd root;sudo passwd --unlock root）
- chmod 777 install.sh
- ./install_all.sh
- su pi
- cd ../../
- python2.7 xiaolan

## 感谢：
- 感谢@陈果果哥哥为小蓝更新了snowboy和修复了snowboy的唤醒词问题
- 感谢@赵磊哥哥为小蓝提供了建议
- 感谢dingdang-robotQQ群中的@绝对零度为小蓝的代码架构做出了概念
- 感谢@蒋小明哥哥为小蓝提供百度离线人脸识别SDK-Linux版本


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
- 小蓝语义理解引擎大更新
- 小蓝语义理解引擎添加文本纠错、分词、依存词法分析、词语相似度分析、短文本相似度分析、关键字提取
- 小蓝语义理解引擎将可以更加准确的判断用户的需求
- 小蓝语义理解转移到云端
- 添加百度离线人脸识别SDK
- 人脸唤醒研发完毕，即将公开
- 语音识别支持远场识别
- 修复一个巨大的BUG
- 代码重构，不再混乱、互相依赖
- 在设置中添加sys_lang，有En(英文)，Zh-Hans(普通话)，Zh-Yue（粤语），Zh-Chun（四川话），通过您的设置来判断语音识别的dev_id，提升用户的体验
- 百度STTRestapi代码重构，支持实时语音识别
- 使用多线程方式支持实时语音识别，对话速度提升至少6秒！
- 添加腾讯语音识别
- 支持腾讯实时语音识别
- 推荐使用腾讯实时语音识别，效率高，但是识别率没有百度高
- 支持简单的手势识别，让聋哑人也能够使用小蓝
- 支持文字识别，提高聋哑人与小蓝交互的效率
- 添加百度人体识别
- 支持腾讯AI开放平台的AI LAB流式语音识别
- pyqt4、pyqt5、wxpython


