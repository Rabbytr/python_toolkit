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

def getfileby_func(dirPath,func=lambda r,f:True):
    '''
    func is a function that defined by you to filter the file
    you wanted to operate
    the function func has two parameter,the directory path of the file
    and the filename
    '''
    file_all = []
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            if func(dirpath,file):
                file_all.append(os.path.join(dirpath, file))
    return file_all

def getfileby_suffix(dirPath,types):
    '''
    types is a list, such as '.jpg','.mp3'
    '''
    files = []
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            if os.path.splitext(file)[1] in types:
                files.append(os.path.join(dirpath,file))
    return files

def del_hidenfile(dirPath):
    gene = os.walk(dirPath)
    for dirpath,dirnames,filenames in gene:
        for file in filenames:
            if file[0] == '.':
                os.remove(os.path.join(dirpath,file))

def get_filesize(dirPath):
    '''
    return the size of a file or all files in a path
    the unit the number that returned is bit
    '''
    if os.path.isfile(dirPath):
        return os.path.getsize(dirPath)
    else:
        gene = os.walk(dirPath)
        filesize = 0
        for dirpath,dirnames,filenames in gene:
            filesize += sum([os.path.getsize(os.path.join(dirpath,filename))\
                             for filename in filenames])
        return filesize

if __name__ == '__main__':
    pass
