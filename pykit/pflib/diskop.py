#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Some function to get the hard drive letter
'''

__author__ = 'Rabbyt'

import os

try:
    import win32file
except ImportError as e:
    print(e)
    print('Please ensure the package pypiwin32 is not installed')
    print('Please install that by type "pip install pypiwin32"')
    os._exit(-1)


  
def getdisk():  
    drives = []  
    sign = win32file.GetLogicalDrives()
    ALLDRIVES = ["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\",
                 "I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\",
                 "Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\",
                 "Y:\\","Z:\\"]  
    for i in range(25):  
        if (sign&1<<i):  
            if win32file.GetDriveType(ALLDRIVES[i]) == \
                win32file.DRIVE_FIXED:  
                drives.append(ALLDRIVES[i])  
    return drives

def getusb():  
    drives = []  
    sign = win32file.GetLogicalDrives()
    ALLDRIVES = ["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\",
                 "I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\",
                 "Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\",
                 "Y:\\","Z:\\"]  
    for i in range(25):  
        if (sign&1<<i):  
            if win32file.GetDriveType(ALLDRIVES[i]) == \
                win32file.DRIVE_REMOVABLE:  
                drives.append(ALLDRIVES[i])  
    return drives

#free_bytes,total_bytes,total_free_bytes=win32file.GetDiskFreeSpaceEx(item)
  
if __name__ == "__main__":
    pass
