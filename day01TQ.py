# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:36:25 2018

@author: Administrator
"""
import urllib.request as r


city_pingyin = input("请输入城市拼音：")

address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pingyin))
info  = r.urlopen(address.format(city_pingyin)).read().decode('utf-8','ignore')
print(info)
#1 查看当前城市天气    #查看其他城市天气  3 保存当前城市天气

menmo = input("请输入菜单：")
if menmo == '1':
    print("1.查看当前城市天气")
if menmo == '2':
    print("2.查看其他城市天气")
if menmo == '3':
    print("3.保存当前城市")