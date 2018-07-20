#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
...
'''

__author__ = 'Rabbyt'

try:
    import requests
except ImportError as e:
    print(e)
    print('The package requests is not installed')
    print('Please install that by type "pip install requests"')
    os._exit(-1)

def download(url,filedir):
    res = requests.get(url,timeout=0.1)
    with open(filedir,'wb') as f:
        f.write(res.content)
    pass
