#!/usr/bin/env python3
import sys
x = len(sys.argv)
if x != 3:
  print('Usage: ./lab2d.py name age')
else: 
  name = str(sys.argv[1])
  age = int(sys.argv[2])
  print('Hi ' + name + ', you are ' + str(age) + ' years old.')

