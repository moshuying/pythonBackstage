# encoding: utf-8
import sys
import datetime

changeFlag = False
with open(sys.argv[1],'r') as f:
    l = f.readlines()
    for i in range(len(l)):
        if l[i].find(sys.argv[2]) != -1:
            if l[i].find(datetime.datetime.now().strftime(sys.argv[3])) != -1:
                sys.exit(0)
            l[i]=sys.argv[2] + datetime.datetime.now().strftime(sys.argv[3]) + '\n'
            changeFlag = True
if changeFlag:
    with open(sys.argv[1],'w') as f:
        f.writelines(l)