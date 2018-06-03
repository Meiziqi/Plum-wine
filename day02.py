# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:39:06 2018

@author: Administrator
"""
a = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
for i in a :
    if i == "星期六":
        print("今天是{}".format(i))
    else:
        print(i)
            

msg = {
 "地址":"5+3",
 "手机号码":"512",
 "寄信人":"你二大爷"
 }

print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])

"""dict(key:value,key:value....)"""

info = {
        "姓名":"谈嘻嘻",
        "性别":"男",
        "身高":"111",
        "年龄":"999"
        }
print(info["姓名"])
print(info["性别"])
print(info["身高"])
print(info["年龄"])

xx = {'name':'土炮儿',
      'sex':'man',
      'songs':['数鸭子','数星星','数狗子'],
      '昵称':['土炮','土农民','土八路']}
songs = xx['songs']
print(songs)


#如果气温哪里是string类型，没有办法输出最大，取消引号
tianqi = {'wendu':['27','24','28','30','31'],
          'tianqi':['小雨转阵雨','小雨','多云','晴','晴转多云'],
          'xingqi':['6','7','1','2','3']
        }
print(max(tianqi['wendu']))
print(tianqi['tianqi'])