#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import re
import shutil

os.system("mkdir data_v1")
# 正则表达式
def subString(txt):
    rule = r'_(.*?)_gra'
    slotList = re.findall(rule, txt)
    return slotList
def subString2(txt2):
    rule2 = r'(.*)_1'
    slotList2 = re.findall(rule2, txt2)
    return slotList2
# 获取文件夹内容
# local_path表示路径

local_path="/var/www/html/PhalApi/public/granary/"
# 返回local_path下所有文件构成的一个list列表
for root,dirs,files in os.walk(local_path):#魂环遍历出该目录下所有子目录中的文件
# filelist=os.listdir(local_path)
#     path = '/home/boon/data_v1'#指定存放图片的目录
# 遍历输出每一个文件的名字和类型
    for item in files:
        # 输出指定后缀类型的文件
        if(item.endswith('.jpg')):
            # 使用正则表达式找到文件名中的时间戳
            slotList = subString(item)
            # 使用正则表达式找到文件名中的IP
            slotList2 = subString2(item)

            # 遍历时间戳
            for timeStamp,slotPath in zip(slotList,slotList2):
                # 将时间戳转化为int
                timeStamp = int(timeStamp)
                # 将时间戳转化为时间
                timeArray = time.localtime(timeStamp)
                # 输出时间中的时
                showTime = int(time.strftime("%H",timeArray))
                # 判断是否时12时
                if showTime == 12:
                # for slot in slotList:
                    # 创建文件夹
                    slotPath = str(slotPath)
                    Path = '/home/boon/data_v1/' + slotPath
                    if not os.path.exists(Path):
                        os.mkdir(Path)
                    # 复制图片
                    shutil.copy(root+'/'+item,Path+'/'+item)
                    print(root+'/'+item) # 使用正则表达式遍历出txt文件的时间戳
                # print(item)
                else:
                    continue
os.system("tar -cf data_v1.tar data_v1/")
os.system("rm -rf  data_v1/")