#!/usr/bin/python3
# -*- coding:utf-8 -*-

from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
