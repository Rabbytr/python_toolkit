#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script is to copy all files of some certain from several disk to
one directory and is just a example

The files that copyed will be stored at the Copyfile directory of the
root directory of the program
'''

__author__ = 'Rabbyt'

import os
import shutil

try:
    from pykit import diskop,pathop
except ImportError as e:
    print(e)
    print('Please ensure the package pykit is existed')
    os._exit(-1)

types = ['.jpg','.png']
#types is the suffixes of files u want to copy
IF_SYSDISK = False
#if scan the disk where the system lives
IF_HIDENFILE = True
#if copy the files that is hiden

def filter_file(path,filename):
    if os.path.splitext(filename)[1] in types:
        if pathop.get_filesize(os.path.join(path,filename)) > 1024*50:
            return True
    return False

def main():
    try:
        os.mkdir('Copyfile')
    except FileExistsError as e:
        pass
    Drives = diskop.getdisk()
    if not IF_SYSDISK:
        if 'C:\\' in Drives:
            Drives.remove('C:\\')
    print(Drives)
    files = []
    for dirPath in Drives:
        print('{}:\nGetting the files...'.format(dirPath))
        files.extend(pathop.getfileby_func(dirPath,filter_file))
    num = len(files)
    count = 0
    try:
        for file in files:
            shutil.copy(file,'.\\Copyfile')
            print(r'{:<20d}/{}'.format(count,num))
            count += 1
            pass
    except:
        print('Maby something wrong')
    if not IF_HIDENFILE:
        pathop.del_hidenfile('.\\Copyfile')
    
if __name__ == '__main__':
    main()

