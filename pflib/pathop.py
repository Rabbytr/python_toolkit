#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Some function to operate the files
'''

__author__ = 'Rabbyt'

import os

def getallfile(dirPath):
    file_all = []
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            file_all.append(os.path.join(dirpath, file))
    return file_all

def getfilebysuffix(dirPath,types):
    '''types is a string list, such as '.jpg','.mp3' '''
    files = []
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            if os.path.splitext(file)[1] in types:
                files.append(os.path.join(dirpath,file))
    return files

def delhidenfile(dirPath):
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            if file[0] == '.':
                os.remove(os.path.join(dirpath,file))

if __name__ == '__main__':
    pass
