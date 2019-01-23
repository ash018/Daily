# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
arr = os.listdir()
x = 0
for filename in os.listdir("."):
    x+=1
    if(filename!='test.py'):
        print (filename)
        print('img'+str(x)+'.jpg')
        os.rename(filename,'img'+str(x)+'.jpg')
        
    
