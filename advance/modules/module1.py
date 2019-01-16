#! /usr/bin/env python3
# -*- coding: utf-8 -*-

' module1 '

__autohor__ = 'zhiguangchen'

import sys

def module1():
    args = sys.argv
    if len(args) == 1:
        print(args)
        print('1 args')
    elif len(args) == 2:
        print(args)
        print('2 args')
    else:
        print(args)
        print('> 2 args')

print(__name__)
if __name__ == '__main__':
    module1()


