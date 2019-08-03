# ********************************************************
# Author        : huangming
# Email         : wangbandi@gmail.com
# Last modified : 2017-09-10 19:54
# Filename      : work.py
# Description   : py3.4
# ********************************************************
import os
import re
# import natsort

path = r'D:\work\stu\update'
pattern = 'Spb\d\.\d\.\d\.[456](?:_upd\d{3})?\(R\).*'
def getpatches(path,pattern):
    filenames = os.listdir(path)
    if not filenames:
        return []
    patch=[]
    for fn in filenames:
        result = re.search(pattern, fn)
        if result:
            patch.append(result.group(0))
    return patch

class Patch():
    def __init__(self,path):
        self.path=path
patch = getpatches(path, pattern)
print(sorted(patch))
