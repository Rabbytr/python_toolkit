### netop
* #### getallfile(dirPath)
返回一个字符串list，即dirPath目录下的所有文件
* #### getfileby_suffix( dirPath, types)
返回一个字符串list，即dirPath下所有类型为types的文件  
types应为一个字符串列表。如 ['.mp3','.jpg']
* #### getfileby_func(dirPath,func=lambda r,f:True)
根据传入的函数过滤得到的文件，不传入默认过滤所有  
函数格式为 func(dirpath,filename),可以对文件位置和路径进行限定
* #### get_filesize(dirPath)
得到文件夹的大小，dirPath为文件路径
* #### del_hidenfile(dirPath)（待改进）
删除dirPath目录下所有隐藏文件

### diskop(win)
* #### getdisk()
返回一个字符串list，得到所有磁盘的根路径
* #### getusb()
返回一个字符串list，得到所有u盘的根路径
