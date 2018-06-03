# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:40:49 2018

@author: Administrator
"""

import urllib.request as r
import json
import time
while 1:
    print("\n",
          "\n",
          "*****欢迎使用Plum-wine天气预报*****\n",
          "**********************************\n"
          " 温馨提示：\n",
          "查看当天城市的天气         请输入  1  \n",
          "查看未来五天城市的天气     请输入  2  \n",
          "保存城市的天气情况         请输入  3  \n",
          "退出系统                  请输入  0  \n")
    menu = input(" 请输入数字：")
    if menu == "0":
        print("你即将退出Plum-wine天气预报")
        time.sleep(2)
        print("*******感谢使用，再见！*******")
        break
    elif menu > "3":
        print(" ********************\n",
              "哈哈哈哈，你输入错了！\n",
              "请输入数字1/2/3")
    elif menu == "1":
        city_pingyin = input("请输入城市的拼音：")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
        info = r.urlopen(url.format(city_pingyin)).read().decode('utf-8','ignore')
        data = json.loads(info)
        TQ1 = {'weather': data['weather'][0]['description'],
              'temp' : data['main']['temp'],
              'temp_min' : data['main']['temp_min'],
              'temp_max' : data['main']['temp_max'],
              'pressure' : data['main']['pressure'],
              }
        state = "*******************\n{}\n天气:     {}\n平均温度:    {}摄氏度\n最高温度:    {}摄氏度\n最低温度:    {}摄氏度\n气压:    {}".format(city_pingyin,TQ1['weather'],TQ1['temp'],TQ1['temp_max'],TQ1['temp_min'],TQ1['pressure'])
        print(state)
        print("*******************\n",
              "*******************\n",
              "请问是否保存到文档\n",
              "是，请输入      Y\n",
              "否，请输入      N")
        save = input("请输入：")
        if save == "Y":
            s = input("请自定义文件名：")
            open("{}.txt".format(s),'w',encoding='utf-8').write(state)
    elif menu == "2":
        city = input("请输入城市的拼音：")
        url1 = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
        info1 = r.urlopen(url1.format(city)).read().decode('utf-8','ignore')
        data1 = json.loads(info1)
        for i in range(len(data1['list'])):
            TQ = {'weather': data1['list'][i]['weather'][0]['description'],
                  'temp' : data1['list'][i]['main']['temp'],
                  'temp_min' : data1['list'][i]['main']['temp_min'],
                  'temp_max' : data1['list'][i]['main']['temp_max'],
                  'pressure' : data1['list'][i]['main']['pressure'],
                  'day' : data1['list'][i]['dt_txt']
                  }
            if data1['list'][i]['dt_txt'][9]==data1['list'][i-1]['dt_txt'][9]:
                print("{}\n天气是{}  平均温度是{}摄氏度  最高温度是{}摄氏度  最低温度是{}摄氏度  气压是{}".format(TQ['day'],TQ['weather'],TQ['temp'],TQ['temp_max'],TQ['temp_min'],TQ['pressure']))
            else:
               # print('日期：{}\n'.format(TQ['day'][0:10]))
                o = "\n\n日期：{}\n\n{}\n天气是{}  平均温度是{}摄氏度  最高温度是{}摄氏度  最低温度是{}摄氏度  气压是{}".format(TQ['day'][0:10],TQ['day'],TQ['weather'],TQ['temp'],TQ['temp_max'],TQ['temp_min'],TQ['pressure'])
                print(o)
        print("*******************\n",
              "*******************\n",
              "请问是否保存到文档\n",
              "是，请输入      Y\n",
              "否，请输入      N")
        save = input("请输入：")
        if save == "Y":
            s = input("请自定义文件名：")
            open("{}.txt".format(s),'w',encoding='utf-8').write(o)
            
                
