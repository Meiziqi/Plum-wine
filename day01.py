# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:28:51 2018

快捷键，字体放大
ctrl +
新建python文件
ctrl +new 
保存

执行代码，选中代码，ctrl + enter
查看python版本Python 3.6.2
@author: yq
"""
#一次申请一个变量
a=3
#一次申明多个变量
xuan,guibin,xixi=80,90,88
xj='小娇'
yanzhi=5.44444444444
#自动补全代码 按  Tab
#TypeError: must be str, not float
print(xj+yanzhi)
#将其他类型转换成字符串类型
b=str(yanzhi)
c='3.9'
d=float(c)
print(xj+str(yanzhi))

print(xj+'\t'+str(yanzhi))

#字符串中出现{}大括号，表示是占位符
print('今天温度是{}天气是{}今天星期{}'.format(10,'小雨','六'))
"""
"""
#列表list,
usemoney=12,20,30,19,20
usemoney[1]
usemoney2=[12,20,30,19,20]
print(usemoney2[0])















