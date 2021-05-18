#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# 压缩体积
# @Date    : 2021-05-18 Tuesday
# @Author  : Radish (minradish@163.com)
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
            # saveImg(img, path, 220)
    except Exception as e:
        raise e

def saveImg(img, path, size = 23):
    (w,h) = img.size;
    # multiple = getMultiple(w, h, size)
    multiple = 1
    if not multiple == -1:
        newImg = img.resize((int(w * multiple), int(h * multiple)), Image.ANTIALIAS)
        saveFileDir = path.replace(INPUT_DIR, OUT_DIR)
        # print(saveFileDir)
        # saveFileDir = saveFileDir.replace('\\', '/')
        outDir = os.path.dirname(saveFileDir);
        # os._exit(0)
        if not os.path.isdir(outDir):
            try:
                os.makedirs(outDir)
            except Exception as e:
                raise e
        try:
            #quality初始压缩比率
            newImg.save(saveFileDir, quality=80)
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
    INPUT_DIR = 'D:/workspace/php/konnastyle/public/uploads'
    OUT_DIR = 'D:/workspace/php/konnastyle/public/uploads/new'
    ergodicDir(INPUT_DIR)
    