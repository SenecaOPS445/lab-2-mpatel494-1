#!/usr/bin/env python3
#Author: Manav Patel
#Author ID: mpatel494
#Date_Created: 25 May 2024
import sys
timer = 3 
if len(sys.argv) == 2:
   timer = int(sys.argv[1])
while timer > 0:
   print(timer)
   timer = timer - 1
print('blast off!')
