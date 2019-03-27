#!/usr/bin/python3
# -*- coding:utf-8 -*-

def func():
    '''
    :return:
    '''
    return "success"


print(func.__doc__)
print(type(func))

f = func
print(f)
print(f())
