#!/usr/bin/python3

import os
import sys
from datetime import datetime
import hashlib

#Function returns date and time of the hash
def getWhen():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

#Function retuns sha256 sum of the given file
def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename,'rb',buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
        return h.hexdigest()

def main():
    outFile = open('outfile.txt','w')
    #os.walk starting at root for all files 
    for root, dirs, files in os.walk('/', topdown=False):
        for name in files:
            name = os.path.join(root,name)
            #ignore certain directories
            if name.startswith('/dev'):
                pass
            elif name.startswith('/proc'):
                pass
            elif name.startswith('/run'):
                pass
            elif name.startswith('/sys'):
                pass
            elif name.startswith('/tmp'):
                pass
            elif name.startswith('/var/lib'):
                pass
            elif name.startswith('/var/run'):
                pass
            else:
                try:
                    #write to the output file
                    string = "Filename: "+name+"\n"+'sha256sum: '+sha256sum(name)+'\n'+'Date & Time: '+getWhen()+'\n\n'
                    outFile.write(string)
                except:
                    continue
    return

main()
