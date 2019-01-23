# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



file = open("testfile.txt","w") 
i = 1 
for i in range(120):
    print(i)
    file.write("data/obj/img"+str(i+1)+".jpg")
    file.write("\n")
 
file.close() 
    
