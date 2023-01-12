# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:56:33 2022

@author: USER
"""

print("成成")
x = input("時薪:")
y = int(x)*6*20
z = y*12
print("年薪:",z)
if(z < 120000*13):
    print("可以換去飛網")
else:
    print("不用換工作") 
    
    
y = input("月薪:")  
z = int(y)*15
print("年薪:",z)
if(z < 120000*13):
    print("可以換去飛網")
else:
    print("不用換工作")
    
print("=="*10)

print("飛網")
a = input("月薪:")
b = int(a)*13
print("年薪:",b)
