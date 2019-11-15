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

path = r'D:\tmp2\001'
pattern = 'Spb(\d)\.(\d)\.(\d)\.(\d)(?:_upd\d{3})?\(R\).*'
def getpatches(path,pattern,minp=None,maxp=None):
    filenames = os.listdir(path)
    if not filenames:
        return []
    patch=[]
    for fn in filenames:
        if 'upd' in fn.lower():
            pattern = '^Spb(\d)\.(\d)\.(\d)\.(\d)_upd(\d{3})\(R\).*'
        else:
            pattern = '^Spb(\d)\.(\d)\.(\d)\.(\d)\(R\).*'
        filepath = os.path.join(path, fn)
        if os.path.isdir(filepath):
            result = re.search(pattern, fn)
            if result:
                numlist = result.groups()
                updnum = '.'+numlist[4] if len(numlist)>4 else ''
                patchnum = float(''.join(numlist[:4])+updnum)
                print(patchnum)
                data = {}
                data['path'] = filepath
                data['name'] = fn
                data['patchnum'] = patchnum
                patch.append(data)
    return patch

class PatchFile():
    def __init__(self, path):
        self.path = path
        self.filepath, self.filename = os.path.split(path)
        name, self.ext = os.path.splitext(self.filename)
        self.patchnum = self.getpatchnum()
        self.ifupd = '_upd' in self.path.lower()

    def getpatchnum(self):
        if self.ifupd:
            pattern = '^Spb(\d)\.(\d)\.(\d)\.(\d)_upd(\d{3})\(R\).*'
        else:
            pattern = '^Spb(\d)\.(\d)\.(\d)\.(\d)\(R\).*'
        result = re.search(pattern, fn)
        if result:
            numlist = result.groups()
            updnum = '.'+numlist[4] if len(numlist)>4 else ''
            patchnum = float(''.join(numlist[:4])+updnum)
            return patchnum
        return 0

class Patch():
    def __init__(self,patchdata):
        self.data=patchdata
        self.path = self.data['path']
        self.root = self.getroot()

    def getroot(self):
        if os.path.isdir(self.path):
            filenames = os.listdir(self.path)
            if 'Spb' == filenames[0][:3]:
                return os.path.join(self.path, filenames[0])
            else:
                return self.path
        return 0

patch = getpatches(path, pattern)
print(sorted(patch, key= lambda x:x['name']))
print(patch[-1])
