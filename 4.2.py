#!/usr/bin/python3
# -*- coding:utf-8 -*-

def fact(n):
    return n * 2


ls = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(ls, key=len))

print(list(map(fact, range(6))))  # [0, 2, 4, 6, 8, 10]

print([fact(n) for n in range(6)])

num_ls = [1, 2, 3]
num = []
print(all(num_ls))
print(all(num))
print(any(num_ls))
print(any(num))
