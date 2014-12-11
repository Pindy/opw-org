#! /usr/bin/python

import sys
import os
import os.path

def list_files(startpath, count=4):
    for f in os.listdir(startpath):
        if f.startswith('.'):
            continue
        else:
            print("{} {}".format('*' * count, f))
            if os.path.isdir(os.path.join(startpath, f)):
                list_files(os.path.join(startpath, f), count + 1)

if __name__ == '__main__':
    list_files(sys.argv[1])
