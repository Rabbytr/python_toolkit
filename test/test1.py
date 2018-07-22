import sys
sys.path.append('../pykit')
import diskop,pathop


def fun(dirpath,file):
    if file[-4:] == '.mp3':
        return True
    return False

print(pathop.get_filesize(r'D:\QQ\MobileFile'))

