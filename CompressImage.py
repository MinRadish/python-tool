#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-07 11:18 Sunday
# @Author  : Radish (1004622952@qq.com)
# @Version : V1.0.0

import os
from PIL import Image

def ergodicDir(fileDir):
    # fileDir = fileDir.replace('\\', '/')
    # print('fileDir:' + fileDir)
    list = os.listdir(fileDir)
    for i in range(0, len(list)):
        if not list[i] == 'textboxio':
            path = os.path.join(fileDir, list[i])
            # print(path)
            if os.path.isdir(path):
                # print('dir')
                # print(os.listdir(path))
                ergodicDir(path)
            elif os.path.isfile(path):
                # print('file');
                compressImage(path)

def compressImage(path):
    try:
        if os.path.splitext(path)[1] in ['.png', '.jpg', 'jpeg', '.PNG', '.JPG', '.JPEG']:
            img = Image.open(path)
            saveImg(img, path)
            saveImg(img, path, 220)
    except Exception as e:
        raise e

def saveImg(img, path, size = 23):
    (w,h) = img.size;
    multiple = getMultiple(w, h, size)
    if not multiple == -1:
        newImg = img.resize((int(w * multiple), int(h * multiple)), Image.ANTIALIAS)
        saveFileDir = path.replace(INPUT_DIR, OUT_DIR + '/' + str(size) + '_' + str(size))
        # saveFileDir = saveFileDir.replace('\\', '/')
        outDir = os.path.dirname(saveFileDir);
        # os._exit(0)
        if not os.path.isdir(outDir):
            try:
                os.makedirs(outDir)
            except Exception as e:
                raise e
        try:
            newImg.save(saveFileDir)
        except Exception as e:
            newImg = newImg.convert('RGB')
            newImg.save(saveFileDir)
        print(saveFileDir)

def getMultiple(width, height, maxSize = 50):
    size = height    
    if width > height:
        size = width
    # if size > maxSize:
    return maxSize / size;
    # else :
        # return -1;

if __name__ == '__main__':
    INPUT_DIR = '/data/wwwroot/www.51wenju.com.cn/public/upload/images'
    OUT_DIR = '/data/wwwroot/www.51wenju.com.cn/public/upload/images'
    ergodicDir(INPUT_DIR)
    