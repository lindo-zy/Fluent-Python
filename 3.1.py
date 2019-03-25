#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import abc

ds = {}
print(isinstance(ds, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))
t1 = (1, 2, [30, 40])

t2 = (1, 2, frozenset([30, 40]))
hash(t2)

dt = {'a': 1, 'b': 2, 'c': 3}
dt.update({'d': 4})
print(dt)

from collections import Counter

ct = 'ashdasdasdhkhk'
print(Counter(ct))
