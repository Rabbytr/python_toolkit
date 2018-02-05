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
    from pflib import diskop,pathop
except ImportError as e:
    print(e)
    print('Please ensure the package pflib is existed')
    os._exit()

types = ['.jpg','.png']
#types is the suffixes of files u want to copy
IF_SYSDISK = False
#if scan the disk where the system lives
IF_HIDENFILE = True
#if copy the files that is hiden

def filter_file(path,filename):
    if os.path.splitext(filename)[1] in types:
        if pathop.get_filesize(os.path.join(path,filename)) > 1024*5:
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
    for dirPath in Drives:
        files = pathop.getfileby_func(dirPath,filter_file)
    try:
        for file in files:
            shutil.copy(file,'.\\Copyfile')
            pass
    except:
        print('Maby something wrong')
    if not IF_HIDENFILE:
        pathop.del_hidenfile('.\\Copyfile')
    
if __name__ == '__main__':
    main()

